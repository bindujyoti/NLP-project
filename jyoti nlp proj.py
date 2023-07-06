from textblob import TextBlob

# define a dictionary that maps sentiment scores to emotions
sentiment_to_emotion = {
    'positive': 'Happiness',
    'neutral': 'Neutral',
    'negative': 'Sadness',
}

# define some sample text
text = "I'm so good today!"

# analyze the sentiment of the text using TextBlob
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

# map the sentiment score to an emotion using the dictionary
if sentiment > 0:
    emotion = sentiment_to_emotion['positive']
elif sentiment == 0:
    emotion = sentiment_to_emotion['neutral']
else:
    emotion = sentiment_to_emotion['negative']

# print the emotion associated with the text
print(emotion)  # Happiness
