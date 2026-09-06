import requests
from .config import Config
class OpenRouterError(RuntimeError): pass
class OpenRouter:
    def __init__(self):
        if not Config.API_KEY or Config.API_KEY == "YOUR_OPENROUTER_KEY_HERE":
            raise OpenRouterError("OPENROUTER_API_KEY is not configured in .env")
    def chat(self, messages, model=None, temperature=0.2, max_tokens=4000):
        models = [model or Config.MODEL] + Config.FALLBACK_MODELS
        last = None
        for selected in dict.fromkeys(models):
            try:
                r = requests.post(Config.API_URL, headers={
                    "Authorization": f"Bearer {Config.API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://127.0.0.1:5000",
                    "X-Title": "CUPESS AI",
                }, json={"model":selected,"messages":messages,"temperature":temperature,"max_tokens":max_tokens}, timeout=120)
                if r.ok:
                    d=r.json()
                    return {"text":d["choices"][0]["message"]["content"],"model":selected,"raw":d}
                last=f"{selected}: HTTP {r.status_code}: {r.text[:500]}"
            except requests.RequestException as e:
                last=f"{selected}: {e}"
        raise OpenRouterError(last or "OpenRouter request failed")
