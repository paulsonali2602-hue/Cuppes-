from pathlib import Path
import subprocess
class Workspace:
    def __init__(self, root):
        self.root=Path(root).resolve(); self.root.mkdir(parents=True,exist_ok=True)
    def path(self, rel):
        p=(self.root/rel).resolve()
        if p!=self.root and self.root not in p.parents: raise ValueError("Path escapes workspace")
        return p
    def tree(self):
        return [str(p.relative_to(self.root))+("/" if p.is_dir() else "") for p in sorted(self.root.rglob("*")) if ".git" not in p.parts and "__pycache__" not in p.parts][:300]
    def write(self, rel, content):
        p=self.path(rel); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8"); return str(p.relative_to(self.root))
    def run(self, command):
        if not command.startswith(("python ","python3 ","pytest","pip ")): raise ValueError("Command blocked")
        r=subprocess.run(command,shell=True,cwd=self.root,text=True,capture_output=True,timeout=60)
        return {"returncode":r.returncode,"stdout":r.stdout[-8000:],"stderr":r.stderr[-8000:]}
