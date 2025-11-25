import pandas as pd

df = pd.read_csv("imdb_movie_dataset.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["Title"])

# Convert numeric columns
df["Revenue (Millions)"] = pd.to_numeric(df["Revenue (Millions)"], errors="coerce")
df["Metascore"] = pd.to_numeric(df["Metascore"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Handle missing values
df["Revenue (Millions)"] = df["Revenue (Millions)"].fillna(df["Revenue (Millions)"].median())
df["Metascore"] = df["Metascore"].fillna(df["Metascore"].median())

# Extract release year properly as integer
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Create runtime numeric
df["Runtime (Minutes)"] = pd.to_numeric(df["Runtime (Minutes)"], errors="coerce")

print("After cleaning:")
print(df.info())
df.to_csv("clean_movies.csv", index=False)
print("\nSaved cleaned dataset → clean_movies.csv")
