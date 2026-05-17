# from fastapi import FastAPI
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
# import numpy as np

# print("🚀 Starting Adaptive Search Engine...")

# app = FastAPI()

# # Load data
# df = pd.read_json("recipes.json")
# texts = df['text'].tolist()

# # Load model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# print("⚡ Generating embeddings...")
# embeddings = model.encode(texts, show_progress_bar=True)

# print("✅ System Ready!")

# # Adaptive weighting
# def get_alpha(query):
#     if len(query.split()) <= 2:
#         return 0.8
#     elif "low" in query:
#         return 0.5
#     else:
#         return 0.2

# # Semantic search
# def semantic_search(query):
#     q_emb = model.encode([query])
#     return cosine_similarity(q_emb, embeddings)[0]

# # Keyword scoring
# def keyword_score(query):
#     scores = []
#     for text in texts:
#         score = sum(word in text.lower() for word in query.lower().split())
#         scores.append(score)
#     return np.array(scores)

# # Normalize
# def normalize(x):
#     return (x - x.min()) / (x.max() - x.min() + 1e-9)

# @app.get("/")
# def home():
#     return {"message": "Adaptive Recipe Search API running 🚀"}

# @app.get("/search")
# def search(query: str):
#     try:
#         alpha = get_alpha(query)

#         bm25 = normalize(keyword_score(query))
#         semantic = normalize(semantic_search(query))

#         final = alpha * bm25 + (1 - alpha) * semantic

#         top_idx = np.argsort(final)[::-1][:10]

#         results = []
#         for i in top_idx:
#             try:
#                 row = df.iloc[i]

#                 results.append({
#                     "name": str(row.get('name', 'N/A')),
#                     "ingredients": str(row.get('ingredients', 'N/A')),
#                     "description": str(row.get('description', 'N/A')),
#                     "steps": str(row.get('steps', 'N/A')),
#                     "minutes": int(row.get('minutes', 0)),
#                     "score": float(final[i]),
#                     "explanation": {
#                         "bm25": float(bm25[i]),
#                         "semantic": float(semantic[i]),
#                         "alpha": alpha
#                     }
#                 })
#             except Exception as row_error:
#                 print("Row error:", row_error)
#                 continue

#         return results

#     except Exception as e:
#         print("Search error:", e)
#         return {"error": str(e)}


from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

print("🚀 Starting Adaptive Search Engine...")

app = FastAPI()

# Load data
df = pd.read_json("recipes.json")
texts = df['text'].tolist()

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

print("⚡ Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

print("System Ready!")

# Adaptive weighting
def get_alpha(query):
    if len(query.split()) <= 2:
        return 0.8
    elif "low" in query:
        return 0.5
    else:
        return 0.2

# Semantic search
def semantic_search(query):
    q_emb = model.encode([query])
    return cosine_similarity(q_emb, embeddings)[0]

# Keyword scoring
def keyword_score(query):
    scores = []
    for text in texts:
        score = sum(word in text.lower() for word in query.lower().split())
        scores.append(score)
    return np.array(scores)

# Normalize
def normalize(x):
    return (x - x.min()) / (x.max() - x.min() + 1e-9)

@app.get("/search")
def search(query: str):

    alpha = get_alpha(query)

    bm25 = normalize(keyword_score(query))
    semantic = normalize(semantic_search(query))

    final = alpha * bm25 + (1 - alpha) * semantic

    top_idx = np.argsort(final)[::-1][:10]

    results = []

    for i in top_idx:
        row = df.iloc[i]

        # 🔥 Correct hybrid logic
        if alpha > 0.7:
            dominance = "Keyword"
        elif alpha < 0.3:
            dominance = "Semantic"
        else:
            dominance = "Hybrid"

        results.append({
            "name": row['name'],
            "ingredients": row['ingredients'],
            "description": row['description'],
            "steps": row['steps'],
            "minutes": int(row['minutes']),
            "score": float(final[i]),
            "bm25": float(bm25[i]),
            "semantic": float(semantic[i]),
            "alpha": alpha,
            "dominance": dominance
        })

    return results