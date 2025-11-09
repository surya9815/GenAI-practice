# 🧠 LangGraph Chatbot

A next-generation **AI Chatbot** built using [LangGraph](https://www.langchain.com/langgraph), combining conversational intelligence, **Retrieval-Augmented Generation (RAG)**, **persistent memory**, **Human-in-the-Loop (HITL)** feedback, **tool integration**, and a beautiful **UI** — all powered by **LangSmith** for tracing and observability.

---

## 🚀 Features

### 💬 Chatting
- Multi-turn conversations with context awareness.
- Persistent memory that carries context across sessions.
- Retry & fallback logic for robust, production-grade behavior.

### 📚 Retrieval-Augmented Generation (RAG)
- Advanced RAG pipeline with:
  - Vector-based and keyword-based retrieval.
  - Long-term memory and knowledge persistence.
  - Human-in-the-Loop (HITL) approval flows for accuracy.
  - Retry and resilience mechanisms for better reliability.

### 🧩 Tools Integration
- Plug-and-play **ToolNodes** for:
  - External API calls
  - Web search
  - Calculations
  - Knowledge base lookups
- Automatic tool routing and orchestration.

### 🧠 Memory, Persistence & HITL
- **Short-term memory** for current sessions.
- **Long-term persistent memory** (via Redis/Postgres/Chroma).
- **Human-in-the-Loop** interface for real-time intervention.
- Memory summarization and compression to save tokens.

### 🧰 LangSmith Integration
- Seamless tracing & observability with **LangSmith**.
- Monitor and debug node flows, message passing, and model performance.
- Visual graph-based workflow inspection.

### 💻 User Interface
- Modern, responsive web interface.
- Built with **React + Tailwind CSS** (or Streamlit alternative).
- Real-time message streaming & typing indicators.
- Conversation history, source documents, and graph visualizations.

---

## 🧱 Architecture Overview

```mermaid
graph TD
  A[User Interface] --> B[LangGraph Engine]
  B --> C[Memory Node]
  B --> D[RAG Node]
  B --> E[Tool Node]
  B --> F[LLM Node]
  C --> G[Database / Vector Store]
  D --> H[Knowledge Base / Documents]
  E --> I[External APIs]
  F --> J[LangSmith for Observability]



MIT License © 2025 Suryansh Thakur
