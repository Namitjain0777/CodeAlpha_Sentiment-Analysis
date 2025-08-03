import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

def get_sentiment(text):
    if not text or not isinstance(text, str): return 'neutral', 0.0
    score = TextBlob(text).sentiment.polarity
    if score > 0.1: return 'positive', score
    elif score < -0.1: return 'negative', score
    return 'neutral', score

def test_tweets():
    print("🔍 TESTING SAMPLE TWEETS\n" + "="*30)
    tweets = [
        "I love this product! It's amazing!", "This is terrible. Worst experience ever.",
        "It's okay, nothing special.", "Best day ever! So happy! 😊",
        "I hate waiting in long lines.", "The weather is nice today.",
        "This app is fantastic and easy to use!", "Disappointed with the service quality.",
        "Not bad, could be better though."
       " anchor doing canvas against modi not fit for journery"
       " slams makers biopic for deliberately using name the god of te ganga",
       " will these channels say modi also scared contests "
        "I am so excited for the new movie release!", "This is the worst book I've ever read.",
        "this new india this indias century because has the most powerful leader in the world",
        "100 sure sir will inform all family and friends ",
      " you will loose your existance election rafel corruption",
       " ‘concierge’ for super rich makes unusual sight ",
       " ’ confused who said that intellectuals should decision",
        "asked learn from how treat minority well does want",
       " for new india can vote for shri narendra modi "
    ]
    for i, t in enumerate(tweets, 1):
        s, score = get_sentiment(t)
        emoji = {"positive": "😊", "negative": "😞", "neutral": "😐"}[s]
        print(f"{i}. {t}\n   {emoji} {s.upper()} (Score: {score:.2f})\n")

def visualize(counts):
    """Display bar and pie chart for sentiment distribution"""
    plt.figure(figsize=(12, 5))

    # Bar Chart
    plt.subplot(1, 2, 1)
    counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title('Sentiment Distribution (Bar)')
    plt.ylabel('Tweet Count')
    plt.xticks(rotation=0)

    # Pie Chart
    plt.subplot(1, 2, 2)
    counts.plot(kind='pie', labels=[f"{i.capitalize()} ({v})" for i, v in counts.items()],
                autopct='%1.1f%%', colors=['green', 'red', 'gray'], startangle=140)
    plt.title('Sentiment Distribution (Pie)')
    plt.ylabel('')

    plt.tight_layout()
    plt.show()

def analyze_file():
    print("📂 ANALYZING FILE\n" + "="*30)
    try:
        path = r"C:\Users\Lenovo\Downloads\Twitter_Data.csv"
        df = pd.read_csv(path)
        col = next((c for c in ['text', 'tweet', 'content'] if c in df.columns), df.columns[0])
        tweets = df[col].dropna().head(100)

        results = [{"tweet": t[:50]+"..." if len(t) > 50 else t,
                    "sentiment": (s:=get_sentiment(t))[0],
                    "score": s[1]} for t in tweets]

        df_res = pd.DataFrame(results)
        counts = df_res['sentiment'].value_counts().reindex(['positive','negative','neutral'], fill_value=0)
        total = len(df_res)

        print(f"✅ Analyzed {total} tweets")
        for label in ['positive', 'negative', 'neutral']:
            print(f"{label.capitalize()}: {counts[label]} ({counts[label]/total*100:.1f}%)")

        best, worst = df_res.loc[df_res['score'].idxmax()], df_res.loc[df_res['score'].idxmin()]
        print(f"\n💚 Best: {best['tweet']} (Score: {best['score']:.2f})")
        print(f"💔 Worst: {worst['tweet']} (Score: {worst['score']:.2f})")

        visualize(counts)
        df_res.to_csv('simple_results.csv', index=False)
        print("💾 Saved: simple_results.csv")

    except Exception as e:
        print(f"❌ Error: {e}")

def custom_text():
    print("✏️  CUSTOM TEXT ANALYSIS\n" + "="*30)
    try:
        while True:
            text = input("Enter text (or 'quit'): ").strip()
            if text.lower() == 'quit': break
            if text:
                s, score = get_sentiment(text)
                emoji = {"positive": "😊", "negative": "😞", "neutral": "😐"}[s]
                print(f"{emoji} {s.upper()} (Score: {score:.2f})\n")
    except KeyboardInterrupt:
        print("\n👋 Exiting...")

# MAIN
if __name__ == "__main__":
    print("🐦 SIMPLE TWITTER SENTIMENT ANALYZER\n" + "="*40)
    test_tweets()
    print("="*40)
    analyze_file()
    print("="*40)
    custom_text()
    print("\n🎉 Done!")
