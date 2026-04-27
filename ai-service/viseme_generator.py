"""
Viseme Generator for Lip Sync
Maps text to viseme sequences for driving the 3D avatar's mouth animations.
Visemes represent mouth shapes corresponding to phoneme groups.
"""

import re
from typing import List, Dict

# Standard viseme mapping based on Microsoft Speech API / Oculus visemes
# Each viseme represents a distinct mouth shape
VISEME_MAP = {
    # Silence
    "sil": 0,     # Mouth closed
    # Vowels
    "aa": 1,      # "father" - open mouth
    "ae": 2,      # "bat" - slightly open
    "ah": 3,      # "but" - mid open
    "ao": 4,      # "bought" - rounded open
    "eh": 5,      # "bet" - mid spread
    "er": 6,      # "bird" - mid rounded
    "ih": 7,      # "bit" - slightly spread
    "iy": 8,      # "beat" - spread
    "ow": 9,      # "boat" - rounded
    "uw": 10,     # "boot" - very rounded
    # Consonants
    "pp": 11,     # p, b, m - lips pressed
    "ff": 12,     # f, v - lower lip to teeth
    "th": 13,     # th - tongue to teeth
    "dd": 14,     # t, d, n - tongue to ridge
    "kk": 15,     # k, g, ng - back tongue
    "ch": 16,     # ch, j, sh - palatal
    "ss": 17,     # s, z - alveolar fricative
    "rr": 18,     # r - retroflex
    "nn": 19,     # l - lateral
}

# Phoneme-to-viseme mapping (simplified English phoneme rules)
PHONEME_TO_VISEME = {
    # Bilabials
    'b': 'pp', 'p': 'pp', 'm': 'pp',
    # Labiodentals
    'f': 'ff', 'v': 'ff',
    # Dentals
    'th': 'th',
    # Alveolars
    't': 'dd', 'd': 'dd', 'n': 'dd',
    # Alveolar fricatives
    's': 'ss', 'z': 'ss',
    # Post-alveolars
    'sh': 'ch', 'ch': 'ch', 'j': 'ch', 'zh': 'ch',
    # Velars
    'k': 'kk', 'g': 'kk', 'ng': 'kk',
    # Liquids
    'l': 'nn', 'r': 'rr',
    # Glides
    'w': 'uw', 'y': 'iy',
    # Glottal
    'h': 'ah',
    # Vowels (simplified)
    'a': 'aa', 'e': 'eh', 'i': 'ih', 'o': 'ao', 'u': 'uw',
}

# Letter combinations to phonemes (simplified)
DIGRAPHS = {
    'th': 'th', 'sh': 'ch', 'ch': 'ch', 'ph': 'ff',
    'ng': 'kk', 'wh': 'uw', 'ck': 'kk', 'qu': 'kk',
    'ee': 'iy', 'oo': 'uw', 'ea': 'iy', 'ou': 'ow',
    'ai': 'ae', 'oa': 'ao', 'ie': 'iy', 'ei': 'ae',
    'aw': 'ao', 'ow': 'ow', 'ew': 'uw',
}


def text_to_visemes(text: str, duration_ms: int = 80) -> List[Dict]:
    """
    Convert text to a sequence of viseme data for lip sync animation.
    
    Args:
        text: Input text to convert
        duration_ms: Duration of each viseme in milliseconds
        
    Returns:
        List of viseme objects with time, viseme_id, and viseme_name
    """
    viseme_sequence = []
    current_time = 0
    
    # Clean text
    text = text.lower().strip()
    words = text.split()
    
    for word_idx, word in enumerate(words):
        # Remove non-alphabetic characters
        clean_word = re.sub(r'[^a-z]', '', word)
        
        if not clean_word:
            continue
        
        i = 0
        while i < len(clean_word):
            # Check for digraphs first
            if i + 1 < len(clean_word):
                digraph = clean_word[i:i+2]
                if digraph in DIGRAPHS:
                    viseme_name = DIGRAPHS[digraph]
                    viseme_id = VISEME_MAP.get(viseme_name, 0)
                    viseme_sequence.append({
                        "time": current_time,
                        "viseme_id": viseme_id,
                        "viseme_name": viseme_name,
                        "duration": duration_ms
                    })
                    current_time += duration_ms
                    i += 2
                    continue
            
            # Single character
            char = clean_word[i]
            phoneme = PHONEME_TO_VISEME.get(char, 'sil')
            viseme_id = VISEME_MAP.get(phoneme, 0)
            
            viseme_sequence.append({
                "time": current_time,
                "viseme_id": viseme_id,
                "viseme_name": phoneme,
                "duration": duration_ms
            })
            current_time += duration_ms
            i += 1
        
        # Add a small pause between words
        viseme_sequence.append({
            "time": current_time,
            "viseme_id": 0,
            "viseme_name": "sil",
            "duration": duration_ms // 2
        })
        current_time += duration_ms // 2
    
    return viseme_sequence


def get_morph_targets(viseme_id: int) -> Dict[str, float]:
    """
    Convert viseme ID to morph target weights for 3D avatar animation.
    These map to Three.js morph targets on the avatar mesh.
    
    Returns a dict of morph target names and their weights (0.0 - 1.0)
    """
    morph_targets = {
        0:  {"jawOpen": 0.0, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.0},  # sil
        1:  {"jawOpen": 0.8, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.2},  # aa
        2:  {"jawOpen": 0.5, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.5},  # ae
        3:  {"jawOpen": 0.4, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.3},  # ah
        4:  {"jawOpen": 0.6, "mouthFunnel": 0.3, "mouthPucker": 0.3, "mouthSmile": 0.0, "mouthStretch": 0.0},  # ao
        5:  {"jawOpen": 0.3, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.6},  # eh
        6:  {"jawOpen": 0.2, "mouthFunnel": 0.3, "mouthPucker": 0.2, "mouthSmile": 0.0, "mouthStretch": 0.0},  # er
        7:  {"jawOpen": 0.2, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.4},  # ih
        8:  {"jawOpen": 0.1, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.6, "mouthStretch": 0.3},  # iy
        9:  {"jawOpen": 0.4, "mouthFunnel": 0.4, "mouthPucker": 0.5, "mouthSmile": 0.0, "mouthStretch": 0.0},  # ow
        10: {"jawOpen": 0.2, "mouthFunnel": 0.6, "mouthPucker": 0.7, "mouthSmile": 0.0, "mouthStretch": 0.0},  # uw
        11: {"jawOpen": 0.0, "mouthFunnel": 0.0, "mouthPucker": 0.4, "mouthSmile": 0.0, "mouthStretch": 0.0},  # pp
        12: {"jawOpen": 0.1, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.2},  # ff
        13: {"jawOpen": 0.1, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.3},  # th
        14: {"jawOpen": 0.1, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.2},  # dd
        15: {"jawOpen": 0.2, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.1},  # kk
        16: {"jawOpen": 0.2, "mouthFunnel": 0.3, "mouthPucker": 0.3, "mouthSmile": 0.0, "mouthStretch": 0.0},  # ch
        17: {"jawOpen": 0.1, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.3, "mouthStretch": 0.3},  # ss
        18: {"jawOpen": 0.2, "mouthFunnel": 0.2, "mouthPucker": 0.2, "mouthSmile": 0.0, "mouthStretch": 0.0},  # rr
        19: {"jawOpen": 0.2, "mouthFunnel": 0.0, "mouthPucker": 0.0, "mouthSmile": 0.0, "mouthStretch": 0.2},  # nn
    }
    
    return morph_targets.get(viseme_id, morph_targets[0])
