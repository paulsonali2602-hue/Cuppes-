import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
class Config:
    API_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
    MODEL = os.getenv("OPENROUTER_MODEL", "cohere/north-mini-code:free").strip()
    FALLBACK_MODELS = [x.strip() for x in os.getenv("OPENROUTER_FALLBACK_MODELS","").split(",") if x.strip()]
    WORKSPACE_DIR = (BASE_DIR / os.getenv("WORKSPACE_DIR","workspace")).resolve()
    MAX_DEBUG_RETRIES = int(os.getenv("MAX_DEBUG_RETRIES","3"))
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
Config.WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
