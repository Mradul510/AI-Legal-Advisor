"""
FastAPI AI Service for LAwBOTie — Legal AI Advisor
Provides NLP-based legal advice with lip-sync viseme data.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from nlp_engine import engine
from viseme_generator import text_to_visemes, get_morph_targets

app = FastAPI(
    title="LAwBOTie AI Service",
    description="AI-powered legal advisor for Indian law with lip-sync support",
    version="1.0.0",
)

# CORS — allow Spring Boot backend and Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Request / Response Models ────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="User's legal query")
    session_id: Optional[str] = Field(None, description="Chat session identifier")


class VisemeData(BaseModel):
    time: int
    viseme_id: int
    viseme_name: str
    duration: int


class EntityData(BaseModel):
    text: str
    label: str
    start: int
    end: int


class ChatResponse(BaseModel):
    response: str
    category: str
    category_name: str
    confidence: float
    intent: str
    entities: List[EntityData]
    key_acts: List[str]
    tips: List[str]
    visemes: List[VisemeData]
    morph_targets: List[Dict[str, float]]


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    nlp_engine: str
    spacy_available: bool


class CategoryResponse(BaseModel):
    categories: Dict[str, str]


# ─── Endpoints ─────────────────────────────────────────────────────────

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint."""
    from nlp_engine import SPACY_AVAILABLE
    return HealthResponse(
        status="healthy",
        service="LAwBOTie AI Service",
        version="1.0.0",
        nlp_engine="spaCy + scikit-learn",
        spacy_available=SPACY_AVAILABLE,
    )


@app.get("/api/categories", response_model=CategoryResponse)
async def get_categories():
    """Get all legal categories."""
    from legal_knowledge import LEGAL_CATEGORIES
    return CategoryResponse(categories=LEGAL_CATEGORIES)


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a legal query and return AI response with lip-sync data.
    
    This endpoint:
    1. Classifies the legal query using scikit-learn
    2. Extracts entities using spaCy NLP
    3. Generates a contextual legal response
    4. Creates viseme data for lip-sync animation
    """
    try:
        # Process with NLP engine
        result = engine.generate_response(request.message)
        
        # Generate lip-sync viseme data for the response
        visemes = text_to_visemes(result["response"], duration_ms=70)
        
        # Generate morph targets for each viseme
        morphs = [get_morph_targets(v["viseme_id"]) for v in visemes]
        
        return ChatResponse(
            response=result["response"],
            category=result["category"],
            category_name=result["category_name"],
            confidence=result["confidence"],
            intent=result["intent"],
            entities=[EntityData(**e) for e in result["entities"]],
            key_acts=result["key_acts"],
            tips=result["tips"],
            visemes=[VisemeData(**v) for v in visemes],
            morph_targets=morphs,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")


@app.post("/api/classify")
async def classify_only(request: ChatRequest):
    """Classify a query without generating a full response."""
    try:
        category, confidence = engine.classify_query(request.message)
        from legal_knowledge import LEGAL_CATEGORIES
        return {
            "category": category,
            "category_name": LEGAL_CATEGORIES.get(category, "General"),
            "confidence": confidence,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/entities")
async def extract_entities(request: ChatRequest):
    """Extract legal entities from text."""
    try:
        entities = engine.extract_entities(request.message)
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/visemes")
async def generate_visemes(request: ChatRequest):
    """Generate viseme data for lip-sync from text."""
    try:
        visemes = text_to_visemes(request.message, duration_ms=70)
        morphs = [get_morph_targets(v["viseme_id"]) for v in visemes]
        return {
            "visemes": visemes,
            "morph_targets": morphs,
            "total_duration": sum(v["duration"] for v in visemes),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── Run ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
