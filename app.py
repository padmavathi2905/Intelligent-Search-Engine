# import streamlit as st
# import requests
# import ast

# st.set_page_config(page_title="Recipe Search", layout="wide")

# # 🎨 Advanced Styling (ANIMATED + HOVER + GLASS EFFECT)
# st.markdown("""
# <style>

# /* Background animation */
# [data-testid="stAppViewContainer"] {
#     background: linear-gradient(-45deg, #f5f7fa, #c3cfe2, #e0c3fc, #8ec5fc);
#     background-size: 400% 400%;
#     animation: gradientBG 12s ease infinite;
# }

# /* 🌈 Background animation keyframes */
# @keyframes gradientBG {
#     0% {background-position: 0% 50%;}
#     50% {background-position: 100% 50%;}
#     100% {background-position: 0% 50%;}
# }

# /* 🧊 Glass card */
# .recipe-card {
#     background: rgba(255, 255, 255, 0.85);
#     backdrop-filter: blur(10px);
#     padding: 20px;
#     border-radius: 18px;
#     box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
#     margin-bottom: 25px;
#     transition: transform 0.3s ease, box-shadow 0.3s ease;
# }

# /* ✨ Hover animation */
# .recipe-card:hover {
#     transform: translateY(-8px) scale(1.02);
#     box-shadow: 0px 20px 40px rgba(0,0,0,0.25);
# }

# /* 🔍 Search bar styling */
# input {
#     border-radius: 12px !important;
#     padding: 10px !important;
# }

# /* 🎯 Titles */
# h1, h2, h3 {
#     color: #333;
# }

# /* 📊 Metrics */
# [data-testid="stMetric"] {
#     background: rgba(255,255,255,0.9);
#     border-radius: 10px;
#     padding: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("🍽️ Adaptive Intelligent Recipe Search")

# query = st.text_input("🔍 Search Recipes")

# if query:

#     # 🔄 Animated loading
#     with st.spinner("✨ Searching delicious recipes..."):
#         try:
#             res = requests.get(
#                 "http://127.0.0.1:8000/search",
#                 params={"query": query},
#                 timeout=10
#             )
#             data = res.json()
#         except:
#             st.error("⚠️ Backend not running")
#             st.stop()

#     # 🎯 Display results
#     for r in data:

#         st.markdown('<div class="recipe-card">', unsafe_allow_html=True)

#         # 🍲 Title
#         st.markdown(f"## 🍲 {r['name']}")
#         st.write(f"⏱️ Time: {r['minutes']} mins")

#         # Description
#         st.write("📝", r['description'])

#         # 🔽 Expanders (clean UI)
#         with st.expander("🥗 Ingredients"):
#             try:
#                 ingredients = ast.literal_eval(r['ingredients'])
#                 for item in ingredients:
#                     st.write(f"• {item}")
#             except:
#                 st.write(r['ingredients'])

#         with st.expander("👩‍🍳 Steps"):
#             try:
#                 steps = ast.literal_eval(r['steps'])
#                 for i, step in enumerate(steps, 1):
#                     st.write(f"Step {i}: {step}")
#             except:
#                 st.write(r['steps'])

#         # 📊 Metrics
#         col1, col2, col3 = st.columns(3)
#         col1.metric("⭐ Score", round(r['score'], 3))
#         col2.metric("🔑 BM25", round(r['explanation']['bm25'], 3))
#         col3.metric("🧠 Semantic", round(r['explanation']['semantic'], 3))

#         # 🔍 Type label
#         alpha = r['explanation']['alpha']

#         if alpha > 0.7:
#             st.success("🔑 Keyword Search Dominant")
#         elif alpha < 0.3:
#             st.info("🧠 Semantic Search Dominant")
#         else:
#             st.warning("⚖️ Hybrid Search")

#         st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import requests
import ast

st.set_page_config(page_title="Recipe Search", layout="wide")

# 🎨 SAME BEAUTIFUL THEME (UNCHANGED)
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #f5f7fa, #c3cfe2, #e0c3fc, #8ec5fc);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.recipe-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    margin-bottom: 25px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.recipe-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0px 20px 40px rgba(0,0,0,0.25);
}

input {
    border-radius: 12px !important;
    padding: 10px !important;
}

h1, h2, h3 {
    color: #333;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.9);
    border-radius: 10px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🍽️ Adaptive Intelligent Recipe Search")

query = st.text_input("🔍 Search Recipes")

if query:

    with st.spinner("✨ Searching delicious recipes..."):
        try:
            res = requests.get(
                "http://127.0.0.1:8000/search",
                params={"query": query},
                timeout=10
            )
            data = res.json()
        except:
            st.error("⚠️ Backend not running")
            st.stop()

    for r in data:

        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)

        # 🍲 Title
        st.markdown(f"## 🍲 {r['name']}")
        st.write(f"⏱️ Time: {r['minutes']} mins")

        # Description
        st.write("📝", r['description'])

        # Ingredients
        with st.expander("🥗 Ingredients"):
            try:
                ingredients = ast.literal_eval(r['ingredients'])
                for item in ingredients:
                    st.write(f"• {item}")
            except:
                st.write(r['ingredients'])

        # Steps
        with st.expander("👩‍🍳 Steps"):
            try:
                steps = ast.literal_eval(r['steps'])
                for i, step in enumerate(steps, 1):
                    st.write(f"Step {i}: {step}")
            except:
                st.write(r['steps'])

        # 📊 Metrics (FIXED — NO explanation)
        col1, col2, col3 = st.columns(3)
        col1.metric("⭐ Score", round(r['score'], 3))
        col2.metric("🔑 BM25", round(r['bm25'], 3))
        col3.metric("🧠 Semantic", round(r['semantic'], 3))

        # 🔥 CORRECT HYBRID DISPLAY
        if r['dominance'] == "Keyword":
            st.success("🔑 Keyword Search Dominant")
        elif r['dominance'] == "Semantic":
            st.info("🧠 Semantic Search Dominant")
        else:
            st.warning("⚖️ Hybrid Search")

        st.markdown('</div>', unsafe_allow_html=True)