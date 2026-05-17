# Adaptive Intelligent Recipe Search

A modern search system that combines keyword-based search and semantic understanding to deliver more relevant and meaningful recipe results.

--------------------------------------------------

## Overview

Traditional search engines rely only on keyword matching, which often fails to capture user intent.  
This project introduces an Adaptive Hybrid Search System that dynamically balances:

- Keyword Search (BM25-like)
- Semantic Search (Sentence Transformers)
- Adaptive Ranking based on query type

--------------------------------------------------

## Key Features

- Smart recipe search (keyword + semantic)
- Adaptive ranking using query understanding
- Explainable results (BM25 vs Semantic scores)
- Full recipe details:
  - Ingredients
  - Steps (step-by-step)
  - Cooking time
  - Description
- Modern UI with:
  - Animated background
  - Expandable sections
  - Hover effects
  - Loading spinner

--------------------------------------------------

## System Architecture

User Query  
   ↓  
Frontend (Streamlit UI)  
   ↓  
Backend API (FastAPI)  
   ↓  
Keyword Search + Semantic Search  
   ↓  
Adaptive Fusion  
   ↓  
Ranked Results  

--------------------------------------------------

## Methodology

1. Keyword Search  
   - BM25-like scoring  
   - Counts matching words  

2. Semantic Search  
   - SentenceTransformer (MiniLM)  
   - Cosine similarity  

3. Adaptive Ranking  

Final Score = α * Keyword + (1 - α) * Semantic  

Where:
- Short queries ("egg") → α = 0.8  
- Mixed queries → α = 0.5  
- Natural language queries → α = 0.2  

--------------------------------------------------

## Dataset

- Source: Food.com Recipes Dataset (Kaggle)

Fields used:
- Name
- Ingredients
- Steps
- Description
- Cooking Time

Preprocessing:
- Removed null values
- Converted lists to strings
- Combined text for search

--------------------------------------------------

## Tech Stack

Frontend: Streamlit  
Backend: FastAPI  
Model: Sentence Transformers  
Data: Pandas  
ML: Scikit-learn  
Language: Python  

--------------------------------------------------

## Installation & Setup

1. Clone repository  
git clone <your-repo-link>  
cd adaptive-search  

2. Create virtual environment  
python3 -m venv venv  
source venv/bin/activate  

3. Install dependencies  
pip install pandas fastapi uvicorn sentence-transformers scikit-learn numpy streamlit requests  

4. Prepare dataset  
python prepare_data.py  

5. Run backend  
uvicorn main:app --reload  

6. Run frontend  
streamlit run app.py  

7. Open app  
http://localhost:8501  

--------------------------------------------------

## 🎥 Demo Usage

Try queries like:
- egg
- healthy breakfast
- low calorie breakfast with eggs

Behavior:
- Short query → keyword search dominates  
- Long query → semantic search dominates  
- Mixed query → hybrid search  

--------------------------------------------------

## 🧪 Evaluation

Compared:
- Keyword-only search  
- Semantic-only search  
- Adaptive hybrid model  

Results:
- Better relevance  
- Handles natural language  
- More meaningful results  

--------------------------------------------------

## 💡 Future Enhancements

- Add food images  
- Add filters (time, ingredients)  
- Favorites system  
- Flutter app integration  
- Learning-to-Rank  
- Deployment  

--------------------------------------------------

## 🏁 Conclusion

This project shows how combining traditional search methods with modern AI improves search quality and user experience.

--------------------------------------------------# project-2-529_teamadaptive
