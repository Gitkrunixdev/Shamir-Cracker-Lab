import os
import json
import csv
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path

from errors import (
    InputFileNotFoundError,
    InputFileEmptyError,
    InputFileFormatError,
    InputDataValidationError,
)
from constants import REQUIRED_FIELDS, SUPPORTED_EXTENSIONS


def load_file(path: str) -> List[Dict[str, Any]]:


Loads a CSV/JSON file and returns a list of records(dictionaries).
Throws readable exceptions for common errors.
p = Path(path)

# 1) Does the file exist?
if not p.exists():
raise InputFileNotFoundError(f"File not found: {path}")

# 2) Is the extension supported?
ext = p.suffix.lower()

if ext not in SUPPORTED_EXTENSIONS:

raise InputFileFormatError(
    f"Unsupported extension: {ext}. Allowed: {SUPPORTED_EXTENSIONS}")

# 3) Is the file empty (size > 0)?

if p.stat().st_size == 0:

raise InputFileEmptyError(f"File is empty: {path}")

# 4) Loading by format

try:

if ext == ".json":

with p.open("r", encoding="utf-8") as f:

data = json.load(f)

if isinstance(data, dict):
    # allow {"records": [...]}

data = data.get("records", [])

if not isinstance(data, list):

raise InputFileFormatError("JSON does not contain a list of records.")

return data

elif ext == ".csv":

with p.open("r", encoding="utf-8") as f:

reader = csv.DictReader(f)

rows = list(reader)

if len(rows) == 0:

raise InputFileEmptyError("CSV has no records.")

return rows

except json.JSONDecodeError as e:

raise InputFileFormatError(f"Invalid JSON: {e}")

except csv.Error as e:

raise InputFileFormatError(f"Invalid CSV: {e}")

except UnicodeDecodeError as e:

raise InputFileFormatError(f"Encoding problem file: {e}")
