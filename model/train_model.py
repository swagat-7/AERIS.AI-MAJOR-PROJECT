import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
# ✨ Extended training dataset
data = {
    "text": [
        "I feel so broken inside", "There’s hope in me still", "My heart hurts", "Let’s go explore the world",
        "I can do this", "I feel so alone", "I need to pray and reflect", "I'm just happy today!",
        "I keep overthinking", "I feel grateful for everything", "I can't stop feeling nervous",
        "I'm in love", "I'm at peace with everything", "I miss someone deeply", "I want to run wild",
        "Life feels heavy", "I want to cry", "I’m ready for anything", "I'm extremely anxious", "Let’s enjoy every moment"
    ],
    "mood": [
        "heartbroken", "hopeful", "heartbroken", "adventurous", 
        "motivated", "lonely", "spiritual", "joyful",
        "worried", "grateful", "anxious",
        "romantic", "blissful", "yearning", "free-spirited",
        "nostalgic", "sad", "motivated", "anxious", "joyful"
    ]
}
# Create dataframe
df = pd.DataFrame(data)
# Create and train model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df["text"], df["mood"])
# Save model
joblib.dump(model, "model/mood_classifier.pkl")
print("✅ Model trained on extended moods and saved as 'mood_classifier.pkl'")