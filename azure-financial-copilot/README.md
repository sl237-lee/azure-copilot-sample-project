# AI Copilot for Financial Insights — Azure AI Foundry Prompt Flows + Fine-Tuning

A demo **enterprise Copilot** built on **Azure AI Foundry**. It showcases:
- **Prompt Flows** for retrieval → reasoning → post-processing
- **Azure OpenAI** (GPT-4o/GPT‑35‑Turbo) for summarization & Q&A
- Optional **fine-tuning** for domain specificity
- A simple **Streamlit** UI to demo the Copilot
- Ready to extend toward **M365 Copilot**/**agentic** workflows

> Tailored for roles requiring **Azure AI Foundry, Copilot, Copilot Studio, prompt engineering, and LLM fine-tuning**.

---

## 🏗️ Architecture

```mermaid
flowchart LR
  A[User Query] --> B[Prompt Flow Input]
  B --> C[Data Retrieval (Python node)]
  C --> D[LLM (Azure OpenAI)]
  D --> E[Post-process (Python node)]
  E --> F[Answer]
  subgraph Azure AI Foundry
    B
    C
    D
    E
  end
  C <--reads--> G[(Azure Blob / Local CSV)]
```

---

## 📂 Repository Layout

```
azure-financial-copilot/
├── README.md
├── requirements.txt
├── promptflow/
│   ├── flow.dag.yaml
│   └── nodes/
│       ├── system_prompt.jinja2
│       ├── data_query.py
│       └── postprocess.py
├── data/
│   ├── portfolio_summary.csv
│   └── train.jsonl
├── scripts/
│   ├── fine_tune.sh
│   └── run_flow_locally.py
└── frontend/
    └── app.py
```

---

## 🚀 Quick Start (Local demo path)

1) **Python env**  
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2) **Azure OpenAI creds**  
Set environment variables (replace with your values):
```bash
export AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com/"
export AZURE_OPENAI_KEY="YOUR_KEY"
export AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"  # or gpt-35-turbo
```

3) **Run local demo (no Foundry required)**  
```bash
python scripts/run_flow_locally.py "Summarize portfolio risk and 3 insights for 2024."
```

4) **Streamlit UI (optional)**
```bash
streamlit run frontend/app.py
```

---

## 🧪 Azure AI Foundry (Prompt Flow) — How to use

1) Create/Use an **AI Foundry Project** in Azure.  
2) In the Foundry portal, create a **Prompt Flow**, then **Import** from `promptflow/flow.dag.yaml`.  
3) Configure the **connection** to your Azure OpenAI deployment in the flow's LLM node.  
4) Attach a **Data connection** to read `data/portfolio_summary.csv` (or point it to Azure Blob).  
5) **Run & Evaluate** in the Foundry UI. Capture screenshots for your README/portfolio.

---

## 🎛️ Fine-Tuning (Optional)

The `data/train.jsonl` contains few-shot examples. You can create your own domain corpus.

```bash
# Login
az login

# Create a fine-tune job (example with gpt-35-turbo)
bash scripts/fine_tune.sh
```

> After completion, set `AZURE_OPENAI_DEPLOYMENT` to your **fine-tuned** deployment name and re-run.

---

## 🧩 Extend to Agentic / M365
- Add **email/Teams/SharePoint** connectors in a new retrieval node.
- Extend the **postprocess** node to return **structured actions** (e.g., create task, draft email).
- Wrap the flow behind an **Azure Function**/**Logic App** for Copilot Plugin integration.

---

## 📸 What to showcase on GitHub
- Screenshots of **Foundry flow graph**, **evaluation metrics**, **Streamlit demo**.
- A short Loom video demo.
- A top-line summary in the README:
  > Built an internal Copilot prototype with Azure AI Foundry prompt flows + fine-tuned GPT for financial insights.
