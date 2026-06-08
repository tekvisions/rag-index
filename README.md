# The RAG Index

A living index of **retrieval-augmented-generation tooling** — RAG frameworks, vector databases,
embeddings, reranking, and ingestion — ranked by **momentum** (stars, push-recency, rising-newness)
computed from live GitHub signals.

Live: https://rag-index.vercel.app · part of [The Living Indexes](https://living-indexes.vercel.app)

## How it works (self-updating)

A daily GitHub Action runs `build_data.py` (searches GitHub across RAG queries, dedupes, filters
to real RAG-stack tools — excluding broad agent platforms and sibling-index repos — categorizes,
scores), `gen_details.py` (one SEO'd page per tool), `gen_og.py`, then `deploy.py` (Vercel REST).

Static HTML/CSS/JS, no framework. "Vector field" aesthetic (Sora + Geist Mono, indigo→magenta).

## Run locally

```bash
GITHUB_TOKEN=... python3 build_data.py
python3 gen_details.py && python3 gen_og.py
python3 -m http.server 8080
```
