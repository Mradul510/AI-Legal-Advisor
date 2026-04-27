"""
NLP Engine — spaCy + scikit-learn based legal query processor.
Handles intent classification, entity extraction, and response generation.
"""

import random
import re
from typing import Dict, List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from legal_knowledge import (
    TRAINING_DATA,
    LEGAL_RESPONSES,
    LEGAL_CATEGORIES,
    GREETINGS,
    FAREWELLS,
)

# Try to load spaCy model; fall back gracefully if not installed
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except (ImportError, OSError):
    SPACY_AVAILABLE = False
    nlp = None


class LegalNLPEngine:
    """
    NLP engine that classifies legal queries, extracts entities,
    and generates contextual responses using Indian legal knowledge.
    """

    def __init__(self):
        self.classifier = self._build_classifier()
        self.greeting_patterns = re.compile(
            r'\b(hi|hello|hey|namaste|good\s*(morning|afternoon|evening)|greetings)\b',
            re.IGNORECASE
        )
        self.farewell_patterns = re.compile(
            r'\b(bye|goodbye|thank\s*you|thanks|see\s*you|farewell)\b',
            re.IGNORECASE
        )

    def _build_classifier(self) -> Pipeline:
        """Build and train the legal category classifier."""
        texts = [t[0] for t in TRAINING_DATA]
        labels = [t[1] for t in TRAINING_DATA]

        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=5000,
                ngram_range=(1, 2),
                stop_words='english'
            )),
            ('clf', MultinomialNB(alpha=0.1))
        ])
        pipeline.fit(texts, labels)
        return pipeline

    def classify_query(self, text: str) -> Tuple[str, float]:
        """
        Classify a legal query into a category.
        Returns (category, confidence).
        """
        proba = self.classifier.predict_proba([text])[0]
        max_idx = proba.argmax()
        category = self.classifier.classes_[max_idx]
        confidence = float(proba[max_idx])
        return category, confidence

    def extract_entities(self, text: str) -> List[Dict]:
        """Extract legal entities and key terms from text using spaCy."""
        entities = []

        if SPACY_AVAILABLE and nlp is not None:
            doc = nlp(text)
            for ent in doc.ents:
                entities.append({
                    "text": ent.text,
                    "label": ent.label_,
                    "start": ent.start_char,
                    "end": ent.end_char,
                })

            # Also extract noun chunks as potential legal terms
            for chunk in doc.noun_chunks:
                if len(chunk.text.split()) >= 2:
                    entities.append({
                        "text": chunk.text,
                        "label": "LEGAL_TERM",
                        "start": chunk.start_char,
                        "end": chunk.end_char,
                    })

        # Simple keyword-based entity extraction as fallback
        legal_keywords = [
            "section", "article", "act", "ipc", "crpc", "bnss", "bns",
            "fir", "pil", "writ", "bail", "rera", "gst", "posh",
            "supreme court", "high court", "district court",
        ]
        text_lower = text.lower()
        for keyword in legal_keywords:
            if keyword in text_lower:
                start = text_lower.index(keyword)
                entities.append({
                    "text": keyword.upper(),
                    "label": "LEGAL_KEYWORD",
                    "start": start,
                    "end": start + len(keyword),
                })

        return entities

    def detect_intent(self, text: str) -> str:
        """Detect the user's intent from their message."""
        if self.greeting_patterns.search(text):
            return "greeting"
        if self.farewell_patterns.search(text):
            return "farewell"

        # Check for question patterns
        question_words = ['what', 'how', 'when', 'where', 'who', 'which', 'can', 'is', 'are', 'do', 'does', 'will', 'should']
        first_word = text.strip().split()[0].lower() if text.strip() else ""
        if first_word in question_words or text.strip().endswith('?'):
            return "question"

        # Check for action-oriented patterns
        action_patterns = re.compile(
            r'\b(file|lodge|register|apply|sue|claim|appeal|complain)\b',
            re.IGNORECASE
        )
        if action_patterns.search(text):
            return "action_request"

        return "information_request"

    def generate_response(self, text: str) -> Dict:
        """
        Process a legal query and generate a comprehensive response.
        Returns a dict with response text, category, entities, etc.
        """
        intent = self.detect_intent(text)

        # Handle greetings
        if intent == "greeting":
            return {
                "response": random.choice(GREETINGS),
                "category": "general",
                "category_name": "General",
                "confidence": 1.0,
                "intent": intent,
                "entities": [],
                "key_acts": [],
                "tips": [],
            }

        # Handle farewells
        if intent == "farewell":
            return {
                "response": random.choice(FAREWELLS),
                "category": "general",
                "category_name": "General",
                "confidence": 1.0,
                "intent": intent,
                "entities": [],
                "key_acts": [],
                "tips": [],
            }

        # Classify query
        category, confidence = self.classify_query(text)
        entities = self.extract_entities(text)
        knowledge = LEGAL_RESPONSES.get(category, LEGAL_RESPONSES["general"])

        # Build contextual response
        response_parts = []

        # Category introduction
        category_name = LEGAL_CATEGORIES.get(category, "General Legal Information")
        if confidence > 0.4:
            response_parts.append(
                f"Based on your query, this falls under **{category_name}**."
            )
        else:
            response_parts.append(
                "Let me help you with that legal question."
            )

        # Overview
        response_parts.append(f"\n\n{knowledge['overview']}")

        # Relevant tips
        relevant_tips = random.sample(knowledge['tips'], min(3, len(knowledge['tips'])))
        if relevant_tips:
            response_parts.append("\n\n**Key Points to Note:**")
            for tip in relevant_tips:
                response_parts.append(f"• {tip}")

        # Relevant acts
        relevant_acts = knowledge['key_acts'][:3]
        if relevant_acts:
            response_parts.append("\n\n**Relevant Legislation:**")
            for act in relevant_acts:
                response_parts.append(f"📜 {act}")

        # Disclaimer
        response_parts.append(
            "\n\n⚖️ *This is AI-generated legal information. For specific legal action, "
            "please consult a qualified advocate.*"
        )

        return {
            "response": "\n".join(response_parts),
            "category": category,
            "category_name": category_name,
            "confidence": confidence,
            "intent": intent,
            "entities": entities,
            "key_acts": knowledge['key_acts'],
            "tips": knowledge['tips'],
        }


# Singleton instance
engine = LegalNLPEngine()
