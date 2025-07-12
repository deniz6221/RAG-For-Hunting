# RAG Implementation Project

A Retrieval-Augmented Generation (RAG) system that processes PDF documents to provide intelligent question-answering capabilities using Google's Gemini AI and ChromaDB for vector storage.

## Overview

This project implements a RAG pipeline that:
- Loads and processes PDF documents from a local directory
- Creates vector embeddings using Google's embedding models
- Stores documents in ChromaDB for efficient similarity search
- Uses Google's Gemini 2.5 Flash model for generating contextual responses
- Implements parent document retrieval for better context preservation

## Features

- **Document Processing**: Automatic PDF loading and text splitting
- **Vector Storage**: ChromaDB integration for similarity search
- **Smart Retrieval**: Parent document retriever with relevance scoring
- **AI-Powered Responses**: Google Gemini integration for natural language generation
- **Automated Web Scraping**: Custom automation script for content collection

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`

3. Place your PDF documents in the `docs/` directory or run modify and run `document_scraper.py`

## Usage

Run the main RAG notebook (`RAG.ipynb`) to:
1. Load and process PDF documents
2. Create vector embeddings and store in ChromaDB
3. Query the knowledge base with natural language questions
4. Receive AI-generated responses based on relevant document content

## Web Scraping Approach

The project includes a non ordinary web scraping component (`document_scraper.py`) that uses mouse and keyboard automation rather than traditional HTTP scraping libraries. This approach was necessary due to:
- Cloudflare bot protection on target websites
- Advanced anti-scraping measures that block automated requests
- The need to simulate genuine user interactions for content access

The scraper automates browser interactions to navigate to URLs, trigger print dialogs, and save content as PDFs for processing.

## File Structure

- `RAG.ipynb` - Main RAG implementation notebook
- `document_scraper.py` - Automated web scraping script
- `requirements.txt` - Python dependencies
- `scrapped_urls.json` - URLs for content collection
- `docs/` - Directory for PDF documents (not included)
- `.env` - Environment variables (not included)

## Important Notes

**Copyright Compliance**: The scraped documents are not included in this repository due to copyright concerns. Users must obtain their own content or ensure they have proper rights to use any documents with this system.

## Dependencies

Key libraries used:
- `langchain` - RAG framework and document processing
- `chromadb` - Vector database for embeddings
- `google-generativeai` - Google Gemini AI integration
- `pypdf` - PDF document processing
- `pynput` - Mouse/keyboard automation for scraping

## License

This project is for educational and research purposes. Ensure compliance with all applicable copyright laws when using with external content.
