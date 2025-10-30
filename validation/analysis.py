from typing import List, Dict, Any

def analyze_share(records: List[Dict[str, Any]]) -> Dict[str, Any]:

"""
Minimal analysis: number of records, average/min/max closing prices.
You can extend this with volume, volatility, simple indicators, etc.
"""
closes = [r["close"] for r in records]
n = len(closes)
avg = sum(closes) / n
mn = min(closes)
mx = max(closes)

symbols = [r["symbol"] for r in records if r.get("symbol")]
symbol_set = sorted(set(symbols)) if symbols else []

return {
    "records_count": n,
    "avg_close": round(avg, 6),
    "min_close": mn,

    "max_close": mx,
    "symbols": symbol_set
}
