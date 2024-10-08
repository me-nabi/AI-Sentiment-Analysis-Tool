from textblob import TextBlob

with open('mytext.txt','r') as f :
    text=f.read()



blob= TextBlob(text)
sentiment= blob.sentiment.polarity 


sentiment_score = ((sentiment + 1) / 2) * 9+1
print(text)
print(f"Sentiment score: {sentiment_score}")
