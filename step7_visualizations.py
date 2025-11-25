import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Movie_Prediction\imdb_movie_dataset.csv"
df = pd.read_csv(file_path)

df = df.dropna(subset=["Revenue (Millions)"]).copy()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Rating", y="Revenue (Millions)")
plt.title("Rating vs Revenue")
plt.savefig("rating_vs_revenue.png")
plt.show()

plt.figure(figsize=(12,5))
df.groupby("Genre")["Revenue (Millions)"].mean().sort_values(ascending=False).plot(kind="bar")
plt.title("Average Revenue by Genre")
plt.xticks(rotation=70)
plt.tight_layout()
plt.savefig("genre_vs_revenue.png")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Runtime (Minutes)", y="Revenue (Millions)")
plt.title("Runtime vs Revenue")
plt.savefig("runtime_vs_revenue.png")
plt.show()

plt.figure(figsize=(8,5))
df.groupby("Year")["Revenue (Millions)"].mean().plot()
plt.title("Revenue Trend Over Years")
plt.savefig("year_vs_revenue.png")
plt.show()
