from typing import Dict

def transform(raw_text: str) -> Dict[str, str]:
    # You can enforce basic formatting, headers, etc.
    cleaned = raw_text.strip()
    # Lightweight guardrail: cap length
    if len(cleaned) > 6000:
        cleaned = cleaned[:6000] + "\n\n[Truncated for length]"
    return {"output": cleaned}
