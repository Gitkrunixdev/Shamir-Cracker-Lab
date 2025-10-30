from typing import List, Dict, Any
from datetime import datetime

from errors import InputDataValidationError
from constants import REQUIRED_FIELDS


def validate_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:


Checks required fields, types, and values. Returns filtered/cleaned records.
Throws InputDataValidationError if the data is unusable.
"""
if not isinstance(records, list):
raise InputDataValidationError("Input data must be a list of records.")

cleaned = []
issues = []

for i, r in enumerate(records):
    # 1) Required fields
missing = [f for f in REQUIRED_FIELDS if f not in r or r[f] in (None, "")]
if missing:
issues.append(f"Record {i}: missing required fields: {missing}")
continue

# 2) Date parsing: accepts ISO or YYYY-MM-DD
date_raw = r["date"]
date_obj = None
for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z"):
try:
date_obj = datetime.strptime(str(date_raw), fmt)
break
except ValueError:
continue
if date_obj is None:
issues.append(f"Record {i}: invalid date format: {date_raw}")
continue

# 3) Closing price: positive number
try:
close_val = float(r["close"])
if close_val <= 0:
issues.append(f"Record {i}: closing price must be > 0 (close={close_val})")
continue
except (ValueError, TypeError):
issues.append(f"Record {i}: field 'close' is not a number: {r['close']}")
continue

# 4) Optional fields (e.g., symbol)
symbol = r.get("symbol", None)
if symbol is not None and not str(symbol).strip():
    # empty string treated as missing
symbol = None

cleaned.append({
    "date": date_obj.date().isoformat(),
    "close": close_val,
    "symbol": symbol
})

if len(cleaned) == 0:
msg = "No valid records after validation."
if issues:
msg += " Issues: " + "; ".join(issues[:5]) + ("..." if len(issues) > 5 else "")
raise InputDataValidationError(msg)

return cleaned
