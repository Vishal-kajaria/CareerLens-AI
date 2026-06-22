# CareerLens AI

AI-powered resume intelligence platform that helps users analyze resumes, identify skill gaps, discover career opportunities, and receive personalized career guidance using LLMs, RAG, and AI agents.

## Features

### Completed ✅

* Resume PDF Upload
* PDF Text Extraction
* Gradio Web Interface
* Modular Python Project Structure

### Planned 🚧

* AI-Powered Resume Analysis
* Resume Match Scoring
* Skill Gap Analysis
* Personalized Career Recommendations
* Live Job Market Search
* Multi-Agent Career Assistant (CrewAI)
* RAG-Powered Career Chatbot
* Analysis History
* PDF Report Generation
* Docker Deployment
* Ollama Local LLM Support

## Tech Stack

### Current

* Python
* Gradio
* PyPDF

### Planned

* OpenAI
* CrewAI
* LangChain
* ChromaDB / Supabase pgvector
* Serper API
* Docker
* Ollama

## Project Structure

```text
CareerLens-AI/
│
├── careerlens/
│   ├── pdf_parser.py
│   ├── ui.py
│   ├── agents.py
│   ├── crew.py
│   ├── rag.py
│   └── ...
│
├── data/
│   ├── uploads/
│   ├── reports/
│   └── vectors/
│
├── main.py
├── requirements.txt
└── README.md
```

## Current Workflow

```text
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Display Results in Browser
```

## Roadmap

### Phase 1 — Resume Extraction ✅

* PDF Upload
* PDF Parsing
* Gradio UI

### Phase 2 — Resume Intelligence

* OpenAI Integration
* Resume Analysis
* Skill Extraction
* Resume Scoring

### Phase 3 — Career Intelligence

* Job Matching
* Skill Gap Detection
* Career Recommendations

### Phase 4 — Agentic AI

* Resume Analyzer Agent
* Career Coach Agent
* Job Research Agent
* Interview Preparation Agent

### Phase 5 — Advanced Features

* RAG
* Vector Database
* Docker Deployment
* Ollama Support

## Project Status

🚧 Active Development
Current Milestone: Resume Upload & Text Extraction Completed
