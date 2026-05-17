import pandas as pd

print("Loading dataset...")

df = pd.read_csv("RAW_recipes.csv")

df = df[['name', 'ingredients', 'description', 'steps', 'minutes']]

df = df.fillna("")

df['name'] = df['name'].astype(str)
df['ingredients'] = df['ingredients'].astype(str)
df['description'] = df['description'].astype(str)
df['steps'] = df['steps'].astype(str)

df['minutes'] = pd.to_numeric(df['minutes'], errors='coerce').fillna(0)

df['text'] = df['name'] + " " + df['ingredients'] + " " + df['description']

df = df.head(2000)

df.to_json("recipes.json", orient="records")

print("Data prepared successfully!")