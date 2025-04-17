import joblib
import pandas as pd
import random
# Load assets
model = joblib.load("model/mood_classifier.pkl")
songs_df = pd.read_csv("data/songs.csv")
quotes_df = pd.read_csv("data/quotes.csv")
def predict_mood(text):
    return model.predict([text])[0]
import pandas as pd
import random
songs_df = pd.read_csv("data/songs.csv")
quotes_df = pd.read_csv("data/quotes.csv")
def recommend_song(mood):
    filtered = songs_df[songs_df['mood'].str.lower() == mood.lower()]
    if not filtered.empty:
        # Randomly return one from all matches
        return filtered.sample(1).iloc[0]
    else:
        return pd.Series({"title": "No Hindi song found", "artist": "N/A"})
def recommend_quote(mood):
    filtered = quotes_df[quotes_df['mood'].str.lower() == mood.lower()]
    if not filtered.empty:
        return filtered.sample(1).iloc[0]
    else:
        return pd.Series({"quote": "No quote found for this mood."})