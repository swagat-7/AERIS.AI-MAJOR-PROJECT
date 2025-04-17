import matplotlib.pyplot as plt
def plot_mood_distribution(mood_data):
    mood_counts = mood_data.value_counts()
    fig, ax = plt.subplots()
    mood_counts.plot(kind='bar', ax=ax, color='#1DB954', edgecolor='black')
    ax.set_title("Mood Distribution")
    ax.set_ylabel("Count")
    ax.set_xlabel("Mood")
    return fig