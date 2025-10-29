# 🧠 AI Copilot for Financial Insights — Azure AI Foundry Prompt Flows + Fine-Tuning

[![Azure](https://img.shields.io/badge/Azure-AI%20Foundry-blue)]()
[![LLM](https://img.shields.io/badge/LLM-GPT--4o%20%7C%20GPT--35--Turbo-lightgrey)]()
[![Python](https://img.shields.io/badge/Built%20With-Python%20%7C%20PromptFlow-green)]()
[![License](https://img.shields.io/badge/License-MIT-brightgreen)]()

---

### 📘 Overview

This project demonstrates how to build an **enterprise-grade Copilot** using **Azure AI Foundry**, **Prompt Flows**, and **Azure OpenAI**.  
It showcases how **prompt engineering**, **LLM orchestration**, and **fine-tuning** can drive contextual insights from business data.

**Use Case:**  
An internal *Financial Insights Copilot* that summarizes portfolio performance, highlights risks, and answers data-driven questions — aligned with enterprise AI enablement roles such as **AI Engineer (Enterprise AI)** at Rockefeller Capital Management.

> Tailored for roles requiring **Azure AI Foundry, Copilot Studio, prompt engineering, and LLM fine-tuning** experience.

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
