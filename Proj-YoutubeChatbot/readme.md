# YouTube Chatbot — README

## Project overview
A lightweight chatbot that answers questions about YouTube videos by transcribing video audio, creating embeddings, and using a retrieval-augmented LLM to generate concise answers and follow-ups.

## Goals
- Provide accurate, context-aware answers about a video.
- Support follow-up Q&A with conversational context.
- Be modular (transcription, embedding, vector store, LLM).

## Key features
- Video metadata & caption extraction
- Speech-to-text fallback for missing captions
- Chunking + embeddings + vector store (semantic retrieval)
- LLM prompt templates for concise answers + follow-up suggestions
- Simple web UI / CLI for testing

## Plan of action (high level)
1. Project scaffolding & dependencies  
2. Video ingestion: URL parsing, metadata, captions retrieval  
3. Transcription pipeline for videos without captions  
4. Text processing: chunking, normalization, embedding generation  
5. Vector store integration (e.g., FAISS, Pinecone, Milvus)  
6. Retrieval & RAG pipeline: prompt templates, LLM integration  
7. UI/UX: minimal web UI or CLI for interactions  
8. Logging, analytics, tests, deployment

## Plan of action — diagram

flowchart TD
    A[User input: video URL / query] --> B[Ingest & Metadata Extraction]
    B --> C{Captions available?}
    C -- Yes --> D[Use captions]
    C -- No --> E[Speech-to-Text Transcription]
    D --> F[Chunking & Preprocessing]
    E --> F
    F --> G[Embeddings]
    G --> H[Vector Store / Index]
    H --> I[Retrieval (relevant chunks)]
    I --> J[LLM Prompting (RAG)]
    J --> K[Response Post-processing]
    K --> L[Return answer + follow-ups to user]
    L --> M[Store session & analytics]
    M --> H[Optional: update vector store]


## Milestones & estimates
- Week 1: Scaffolding, basic ingestion, captions extraction (2–3 days)  
- Week 2: Transcription integration + basic chunking/embedding (3–4 days)  
- Week 3: Vector store & retrieval + simple RAG pipeline (4–5 days)  
- Week 4: UI + end-to-end testing + analytics (4–6 days)

## Minimal dev/run instructions
1. Create a virtual env and install dependencies (transcription, embedding, vector store, LLM SDK).  
2. Set API keys (speech-to-text, embedding model, LLM, vector DB) via env vars.  
3. Run ingestion script for a sample video to generate embeddings.  
4. Start the small web server or CLI to query the chatbot.

## Directory suggestions
- /ingest — video ingestion & transcription  
- /embeddings — chunking + embedding scripts  
- /index — vector store helpers  
- /api — retrieval + LLM prompts  
- /ui — minimal web UI / CLI  
- /tests — integration/unit tests

## Notes
- Use modular interfaces to swap providers (OpenAI, local LLMs, Pinecone/FAISS).  
- Keep prompt templates small and include context window checks.  
- Add rate-limiting & cache for repeated video requests.



youtube -> transcript (YT API)-> chunks and store in vector store -> then Retrival -> Augmentation -> Generation

