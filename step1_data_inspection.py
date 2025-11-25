import pandas as pd

df = pd.read_csv("imdb_movie_dataset.csv", low_memory=False)

print("Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nSample Rows:\n")
print(df.head(10))
