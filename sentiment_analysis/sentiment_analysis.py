from textblob import TextBlob

print("=== Sentiment Analysis Tool ===")

text = input("Enter your review or sentence: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

print("\nPolarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive 😊")

elif polarity < 0:
    print("Sentiment: Negative 😞")

else:
    print("Sentiment: Neutral 😐")