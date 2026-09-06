import json,re
from .openrouter import OpenRouter
from .tools import Workspace
from .config import Config
class CupessAgent:
    def __init__(self):
        self.llm=OpenRouter(); self.ws=Workspace(Config.WORKSPACE_DIR)
    def chat(self,text):
        r=self.llm.chat([{"role":"system","content":"You are CUPESS AI, a concise helpful coding assistant."},{"role":"user","content":text}])
        return r["text"],{"mode":"chat","model":r["model"]}
    def plan(self,task):
        r=self.llm.chat([{"role":"system","content":"Return JSON only with goal, steps, files, tests."},{"role":"user","content":task}],max_tokens=2500)
        try:return json.loads(r["text"]),r["model"]
        except:return {"goal":task,"steps":[r["text"]],"files":[],"tests":[]},r["model"]
    def run_task(self,task):
        events=[]; plan,pm=self.plan(task); events.append({"stage":"planner","model":pm,"data":plan})
        r=self.llm.chat([{"role":"system","content":"Return JSON only: {files:[{path,content}]}. Create complete files for the task."},{"role":"user","content":f"Task: {task}\nPlan: {json.dumps(plan)}\nWorkspace: {self.ws.tree()}"}],max_tokens=7000)
        try: obj=json.loads(r["text"])
        except:
            m=re.search(r"\{.*\}",r["text"],re.S); obj=json.loads(m.group(0)) if m else {"files":[]}
        written=[]
        for f in obj.get("files",[]):
            if "path" in f and "content" in f: written.append(self.ws.write(f["path"],f["content"]))
        events.append({"stage":"coder","model":r["model"],"files":written})
        review=self.llm.chat([{"role":"system","content":"Review this coding task. Reply PASS if no obvious issue; otherwise list concrete issues."},{"role":"user","content":f"Task: {task}\nFiles: {written}"}],max_tokens=2000)
        events.append({"stage":"reviewer","model":review["model"],"data":review["text"]})
        return f"Task completed. Files: {', '.join(written) if written else 'none'}",events
