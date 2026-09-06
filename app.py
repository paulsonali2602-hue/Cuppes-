from flask import Flask,request,jsonify,render_template
from .agent import CupessAgent
from .config import Config
def create_app():
    app=Flask(__name__,template_folder="../ui",static_folder="../ui/static")
    agent=CupessAgent()
    @app.get("/")
    def index(): return render_template("index.html")
    @app.post("/api/chat")
    def chat():
        d=request.get_json(silent=True) or {}; text=str(d.get("message","")).strip()
        if not text:return jsonify({"error":"Message is empty"}),400
        try:
            if d.get("mode")=="agent": a,e=agent.run_task(text)
            else: a,m=agent.chat(text); e=[m]
            return jsonify({"answer":a,"events":e})
        except Exception as ex:return jsonify({"error":str(ex)}),500
    @app.get("/api/status")
    def status(): return jsonify({"name":"CUPESS AI","version":"1.0.0","model":Config.MODEL,"api_configured":bool(Config.API_KEY and Config.API_KEY!="YOUR_OPENROUTER_KEY_HERE")})
    return app
