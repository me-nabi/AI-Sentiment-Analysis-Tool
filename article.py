from textblob import TextBlob
from newspaper import Article

url = 'https://indianexpress.com/article/cities/mumbai/man-killed-blackmail-thane-woman-intimate-photos-9603638/'
article=Article(url)

article.download()
article.parse()

article.nlp()

text= article.summary
print(text)

blob= TextBlob(text)
sentiment= blob.sentiment.polarity 

sentiment_score = ((sentiment + 1) / 2) * 9 + 1
print(f"Sentiment score: {sentiment_score}")
