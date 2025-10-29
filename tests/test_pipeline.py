json import
from pathlib import Path

from main import run_pipeline

assert res["status"] == "ok" 
assert Path(res["json_report"]).exists() 
assert Path(res["txt_report"]).exists() 

payload = json.loads(Path(res["json_report"]).read_text(encoding="utf-8")) 
assert payload["analysis"]["records_count"] == 2 
assert payload["analysis"]["avg_close"] == 15.0 
assert payload["analysis"]["min_close"] == 10.0 
assert payload["analysis"]["max_close"] == 20.0

def test_empty_file(tmp_path): 
data_dir = tmp_path / "data" 
data_dir.mkdir() 
empty_file = data_dir / "empty.csv" 
empty_file.write_text("", encoding="utf-8") 

res = run_pipeline(str(empty_file), out_dir=str(tmp_path / "reports"), base_name="empty") 
assert res["status"] == "error" 
assert res["error_type"] == "InputFileEmptyError"

def test_bad_json(tmp_path): 
data_dir = tmp_path / "data" 
data_dir.mkdir() 
bad_json = data_dir / "bad.json" 
bad_json.write_text("{ this is not valid json }", encoding="utf-8") 

res = run_pipeline(str(bad_json), out_dir=str(tmp_path / "reports"), base_name="badjson") 
assert res["status"] == "error" 
assert res["error_type"] == "InputFileFormatError"


