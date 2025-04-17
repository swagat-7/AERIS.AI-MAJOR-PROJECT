import streamlit as st
from utils import predict_mood, recommend_song, recommend_quote
from mood_chart import plot_mood_distribution
import pandas as pd
st.set_page_config(page_title="AERIS.AI", layout="centered")
st.title(" AERIS.AI")
st.header("Built on emotions , backed by AI ")
# Mood list
available_moods = [
    "joyful", "heartbroken", "hopeful", "lonely", "spiritual", "motivated", "nostalgic",
    "romantic", "yearning", "anxious", "worried", "grateful", "blissful", "free-spirited", "adventurous"
]
# Mood history session
if 'mood_history' not in st.session_state:
    st.session_state.mood_history = []
# Mood detection via text (can be disabled by removing this block)
# Instead of detecting via text input, we directly rely on the dropdown for mood selection
detected_mood = None
user_input = ""  # Removed text input
# Dropdown override
selected_mood = st.selectbox("🎛️ Choose your mood:", options=available_moods)
# You can still include detected mood if needed in the future (based on user input or any other automatic mechanism)
if detected_mood:  
    st.success(f"Detected Mood: **{detected_mood}**")
# Final mood determination
final_mood = selected_mood or detected_mood
if final_mood:
    st.session_state.mood_history.append(final_mood)
    song = recommend_song(final_mood)
    quote = recommend_quote(final_mood)
    st.subheader("🎶 Song Recommendation:")
    st.write(f"**{song['title']}** by *{song['artist']}*")
    st.subheader("💬 Quote Recommendation:")
    st.write(f"*{quote['quote']}*")
# Analytics dropdown
with st.expander("📊 Show Mood Analytics", expanded=False):
    if st.session_state.mood_history:
        st.subheader("🧠 Mood Capsules:")
        for m in st.session_state.mood_history:
            st.markdown(
                f"<span style='background-color:#1DB954;padding:6px 15px;border-radius:30px;color:white;margin:5px;display:inline-block;'>{m}</span>",
                unsafe_allow_html=True
            )
        st.subheader("📉 Mood Frequency Chart:")
        mood_series = pd.Series(st.session_state.mood_history)
        fig = plot_mood_distribution(mood_series)
        st.pyplot(fig)
    else:
        st.info("No mood data to display yet.")