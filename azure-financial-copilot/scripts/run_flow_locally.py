import os, sys, pandas as pd
from typing import Dict
from dotenv import load_dotenv
from openai import AzureOpenAI

# local reuse of the nodes
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "promptflow" / "nodes"))
import data_query as dq  # type: ignore

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")

def chat_completion(system: str, user: str) -> str:
    client = AzureOpenAI(
        api_version="2024-10-01-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
    )
    resp = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {"role":"system","content":system},
            {"role":"user","content":user}
        ],
        temperature=0.2,
        max_tokens=800
    )
    return resp.choices[0].message.content

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_flow_locally.py \"<your question>\"")
        sys.exit(1)
    user_query = sys.argv[1]

    # Step 1: system prompt
    system_prompt = "You are a financial insights assistant. Be concise, factual, and add bullet points for insights."

    # Step 2: data retrieval
    ctx = dq.transform(query=user_query, data_path=str(Path(__file__).resolve().parents[1] / "data" / "portfolio_summary.csv"))
    context = ctx.get("context", "No context.")

    # Step 3: LLM
    prompt = f"""Context (CSV-derived):
{context}

User question:
{user_query}

Provide a helpful, well-structured answer grounded in the context. If unknown, say so.
"""
    answer = chat_completion(system_prompt, prompt)

    # Step 4: postprocess (simple)
    answer = answer.strip()
    print("\n=== ANSWER ===\n")
    print(answer)

if __name__ == "__main__":
    main()
