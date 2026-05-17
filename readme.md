# Adaptive Intelligent Recipe Search

A search system that combines keyword-based retrieval and semantic understanding to deliver more relevant and meaningful recipe results.

--------------------------------------------------

## Overview

Traditional search engines rely on exact keyword matching, which often fails to capture user intent. This project introduces an Adaptive Hybrid Search System that dynamically balances keyword search and semantic search using a query-aware ranking strategy.

--------------------------------------------------

## Key Features

- Hybrid recipe search combining keyword and semantic methods  
- Adaptive ranking based on query characteristics  
- Explainable results with keyword and semantic scores  
- Detailed recipe output including ingredients, steps, time, and description  
- Interactive user interface with expandable sections and loading feedback  

--------------------------------------------------

## System Architecture

User Query  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
Keyword Search and Semantic Search  
↓  
Adaptive Fusion  
↓  
Ranked Results  

--------------------------------------------------

## Methodology

The system combines keyword-based and semantic retrieval using a hybrid scoring function:

Final Score = α × Keyword + (1 - α) × Semantic  

Keyword Search uses a BM25-style approach that counts query term matches.  
Semantic Search uses SentenceTransformer embeddings with cosine similarity.  

Adaptive Ranking adjusts the value of α based on the query:

Short queries → α = 0.8  
Mixed queries → α = 0.5  
Natural language queries → α = 0.2  

--------------------------------------------------

## Dataset

Source: Food.com Recipes Dataset from Kaggle  

Fields used:
Name  
Ingredients  
Steps  
Description  
Cooking Time  

Preprocessing:
Removed missing values  
Converted lists to strings  
Combined fields into searchable text  

--------------------------------------------------

## Tech Stack

Frontend: Streamlit  
Backend: FastAPI  
Model: Sentence Transformers  
Data Processing: Pandas  
Machine Learning: Scikit-learn  
Language: Python  

--------------------------------------------------

## Installation and Setup

git clone <your-repo-link>  
cd adaptive-search  

python3 -m venv venv  
source venv/bin/activate  

pip install pandas fastapi uvicorn sentence-transformers scikit-learn numpy streamlit requests  

python prepare_data.py  

uvicorn main:app --reload  

streamlit run app.py  

Open in browser:  
http://localhost:8501  

--------------------------------------------------

## Demo Usage

Example queries:
egg  
healthy breakfast  
low calorie breakfast with eggs  

Behavior:
Short query → Keyword dominant  
Long query → Semantic dominant  
Mixed query → Hybrid search  

--------------------------------------------------

## Evaluation

The system is evaluated by comparing keyword-only, semantic-only, and hybrid retrieval methods.

Results show improved relevance, better handling of natural language queries, and balanced precision and recall using the hybrid approach.

--------------------------------------------------

## Future Enhancements

Add image support for recipes  
Introduce filtering by time and ingredients  
Implement personalization features  
Improve ranking using learning-based methods  
Deploy system for public access  

--------------------------------------------------

## Conclusion

This project demonstrates that combining traditional information retrieval techniques with modern semantic models improves search performance and user experience.

--------------------------------------------------

## Authors

Padmavathi Kadium  

California State University, Long Beach  

--------------------------------------------------

## Note

The original dataset is not included due to size limitations.  
Download the dataset from Kaggle and run:

Link for dataset - https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions

python prepare_data.py
