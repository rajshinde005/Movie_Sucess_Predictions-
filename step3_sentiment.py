import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER if not already downloaded
nltk.download('vader_lexicon')

# Load dataset
df = pd.read_csv(r"C:\Movie_Prediction\imdb_movie_dataset.csv")

# Drop rows without reviews
df = df.dropna(subset=["User_Reviews"])

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Define function
def get_sentiment(review):
    score = sid.polarity_scores(review)
    return pd.Series([score['pos'], score['neg'], score['neu'], score['compound']])

df[["Positive", "Negative", "Neutral", "Sentiment_Score"]] = df["User_Reviews"].apply(get_sentiment)

# Save output
df.to_csv(r"C:\Movie_Prediction\sentiment_scores.csv", index=False)

print("Sentiment analysis completed 🎉")
print("Sentiment file saved at: C:\\Movie_Prediction\\sentiment_scores.csv")
