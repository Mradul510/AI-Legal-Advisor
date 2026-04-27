try:
    import fastapi
    print("fastapi OK")
except ImportError as e:
    print(f"fastapi FAIL: {e}")

try:
    import uvicorn
    print("uvicorn OK")
except ImportError as e:
    print(f"uvicorn FAIL: {e}")

try:
    from nlp_engine import engine
    print("nlp_engine OK")
except Exception as e:
    print(f"nlp_engine FAIL: {e}")

try:
    from viseme_generator import text_to_visemes
    print("viseme_generator OK")
except Exception as e:
    print(f"viseme_generator FAIL: {e}")

print("All checks done")
