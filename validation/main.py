from io_utils import load_file
from validation import validate_records
from analysis import analyze_share
from report import build_report_payload, save_report_json, save_report_txt
from errors import (
    InputFileNotFoundError,
    InputFileEmptyError,
    InputFileFormatError,
    InputDataValidationError,
)


def run_pipeline(input_path: str, out_dir: str = "reports", base_name: str = "result"):


try:
raw = load_file(input_path)
records = validate_records(raw)
analysis = analyze_share(records)
payload = build_report_payload(input_path, analysis)

json_path = f"{out_dir}/{base_name}.json"
txt_path = f"{out_dir}/{base_name}.txt"

save_report_json(payload, json_path)
save_report_txt(payload, txt_path)

return {
    "status": "ok",
    "json_report": json_path,
    "txt_report": txt_path,
    "summary": analysis
}

except (InputFileNotFoundError, InputFileEmptyError, InputFileFormatError, InputDataValidationError) as e:
return {
    "status": "error",
    "error_message": str(e),
    "error_type": e.__class__.__name__
}

if __name__ == "__main__":
result = run_pipeline("data/sample.csv", out_dir="reports",
                      base_name="sample_run")
print(result)
