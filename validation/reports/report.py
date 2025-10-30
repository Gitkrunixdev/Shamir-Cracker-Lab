from typing import Dict, Any
from pathlib import Path
from datetime import datetime
eport.py

json import


def build_report_payload(source_path: str, analysis: Dict[str, Any]) -> Dict[str, Any]:


return {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "source_file": str(source_path),
    "analysis": analysis
}


def save_report_json(payload: Dict[str, Any], out_path: str) -> str:


p = Path(out_path)
p.parent.mkdir(parents=True, exist_ok=True)
with p.open("w", encoding="utf-8") as f:
json.dump(payload, f, ensure_ascii=False, indent=2)
return str(p)


def save_report_txt(payload: Dict[str, Any], out_path: str) -> str:


p = Path(out_path)
p.parent.mkdir(parents=True, exist_ok=True)
lines = [
    f"generated_at: {payload['generated_at']}",
    f"source_file: {payload['source_file']}",
    "analysis:",
    f" records_count: {payload['analysis']['records_count']}",
    f" avg_close: {payload['analysis']['avg_close']}",
    f" min_close: {payload['analysis']['min_close']}",
    f" max_close: {payload['analysis']['max_close']}",
    f" symbols: {', '.join(payload['analysis']['symbols']) if payload['analysis']['symbols'] else '(none)'}"
]
with p.open("w", encoding="utf-8") as f:
f.write("\n".join(lines) + "\n")
return str(p)
