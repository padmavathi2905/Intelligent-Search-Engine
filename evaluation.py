from sklearn.metrics import precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# =========================
# QUERY 1: eggs
# =========================
y_true_eggs = [1,1,0,1,1,1,0,1,1,1]

y_keyword_eggs = [1,1,1,1,1,1,1,1,1,1]
y_semantic_eggs = [1,1,1,1,1,1,1,1,1,1]
y_hybrid_eggs = [1,1,1,1,1,1,1,1,1,1]

# =========================
# QUERY 2: breakfast with eggs
# =========================
y_true_breakfast = [1,1,1,1,1,1,0,1,1,1]

y_keyword_breakfast = [1,0,0,0,1,1,0,0,0,1]
y_semantic_breakfast = [1,1,1,1,1,1,1,1,1,1]
y_hybrid_breakfast = [1,1,1,1,1,1,0,1,1,1]

# =========================
# QUERY 3: low calorie breakfast with eggs
# =========================
y_true_lowcal = [1,1,1,1,1,1,1,1,1,1]

y_keyword_lowcal = [0,1,0,0,0,0,0,0,0,0]
y_semantic_lowcal = [1,1,1,1,1,1,1,1,1,1]
y_hybrid_lowcal = [1,1,1,1,1,1,1,1,1,1]

# =========================
# COMBINE ALL QUERIES
# =========================
y_true = y_true_eggs + y_true_breakfast + y_true_lowcal
y_keyword = y_keyword_eggs + y_keyword_breakfast + y_keyword_lowcal
y_semantic = y_semantic_eggs + y_semantic_breakfast + y_semantic_lowcal
y_hybrid = y_hybrid_eggs + y_hybrid_breakfast + y_hybrid_lowcal

# =========================
# EVALUATION FUNCTION
# =========================
def evaluate(name, y_pred):
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(name)
    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1 Score:", round(f1, 3))
    print()

    return precision, recall, f1

# =========================
# COMPUTE METRICS
# =========================
p_k, r_k, f_k = evaluate("Keyword", y_keyword)
p_s, r_s, f_s = evaluate("Semantic", y_semantic)
p_h, r_h, f_h = evaluate("Hybrid", y_hybrid)

# =========================
# GRAPH
# =========================
methods = ["Keyword", "Semantic", "Hybrid"]

precision = [p_k, p_s, p_h]
recall = [r_k, r_s, r_h]
f1 = [f_k, f_s, f_h]

x = range(len(methods))

plt.figure(figsize=(6,4))

plt.plot(x, precision, marker='o', label="Precision")
plt.plot(x, recall, marker='o', label="Recall")
plt.plot(x, f1, marker='o', label="F1 Score")

plt.xticks(x, methods)
plt.xlabel("Methods")
plt.ylabel("Score")
plt.title("Performance Comparison of Retrieval Methods")

plt.legend()

# Save graph for paper
plt.savefig("performance_comparison.png")

plt.show()