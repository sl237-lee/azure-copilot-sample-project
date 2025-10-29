import pandas as pd
import json
from typing import Dict, Any

def transform(query: str, data_path: str) -> Dict[str, Any]:
    """
    Reads a portfolio CSV and returns a compact context string relevant to the query.
    CSV columns: client, year, aum, return_pct, risk_score, notes
    """
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        return {"context": f"Could not load data: {e}.", "rows": 0}

    # naive filter: keep latest year rows and small sample
    latest_year = int(df["year"].max()) if "year" in df.columns else None
    if latest_year:
        dff = df[df["year"] == latest_year].copy()
    else:
        dff = df.copy()

    # simple relevance: if query contains client names or keywords
    keys = [k.strip().lower() for k in query.split() if len(k) > 3]
    def score_row(row):
        text = " ".join([str(row.get(c, "")) for c in df.columns]).lower()
        return sum(k in text for k in keys)

    dff["score"] = dff.apply(score_row, axis=1)
    dff = dff.sort_values("score", ascending=False).head(8)

    # Build a compact context block
    cols = ["client", "year", "aum", "return_pct", "risk_score", "notes"]
    cols = [c for c in cols if c in dff.columns]
    lines = []
    for _, r in dff[cols].iterrows():
        line = ", ".join(f"{c}={r[c]}" for c in cols)
        lines.append(line)

    context = " | ".join(lines) if lines else "No matching rows."
    return {"context": context, "rows": len(dff)}
