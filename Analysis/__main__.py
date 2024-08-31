from dotenv import load_dotenv
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os

def analyzeText(text):
    return sia.polarity_scores(text=text)

def analyzeArrayOfTweets(tweets, fileName):
    result = []
    for index, tweet in enumerate(tweets):
        print(f"Processing ${index} out of ${len(tweets)}")
        score = analyzeText(tweet['text'])
        result.append({
            'tweet': tweet['text'],
            'id': tweet['id'],
            'compound': score['compound'],
            'positive': score['pos'],
            'neutral': score['neu'],
            'negative': score['neg']      
        })
    with open(f'analysis/{fileName}', 'w') as file:
        json.dump(result, file, indent=4)

if __name__ == '__main__':
    load_dotenv()
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    filesToRead = os.listdir('./data')
    for fileName in filesToRead:
        tweets = []
        with open(f"data/{fileName}") as file:
            tweets = json.load(file)
        analyzeArrayOfTweets(tweets=tweets, fileName=fileName)
        

