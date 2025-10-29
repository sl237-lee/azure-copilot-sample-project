import os
from pathlib import Path
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import sys

# local nodes
sys.path.append(str(Path(__file__).resolve().parents[1] / "promptflow" / "nodes"))
import data_query as dq  # type: ignore

load_dotenv()

st.set_page_config(page_title="Financial Copilot (Azure AI Foundry Demo)")

st.title("💼 Financial Copilot — Azure AI Foundry Demo")
st.write("Ask about portfolio risk, performance, or 2024 highlights. The app retrieves compact CSV context, then asks Azure OpenAI for a grounded answer.")

query = st.text_input("Your question", "Summarize portfolio risk and 3 insights for 2024.")
run = st.button("Run")

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

if run:
    if not AZURE_OPENAI_ENDPOINT or not AZURE_OPENAI_KEY:
        st.error("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY environment variables.")
    else:
        system_prompt = "You are a financial insights assistant. Be concise, factual, and add bullet points for insights."
        ctx = dq.transform(query=query, data_path=str(Path(__file__).resolve().parents[1] / "data" / "portfolio_summary.csv"))
        context = ctx.get("context", "No context.")

        prompt = f"""Context (CSV-derived):
{context}

User question:
{query}

Provide a helpful, well-structured answer grounded in the context. If unknown, say so.
"""
        answer = chat_completion(system_prompt, prompt)
        st.subheader("Answer")
        st.markdown(answer)
