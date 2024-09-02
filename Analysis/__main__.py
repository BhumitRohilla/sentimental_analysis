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
        score = analyzeText(tweet['Message'])
        result.append({
            'tweet': tweet['Message'],
            'id': tweet['tweetId'],
            'compound': score['compound'],
            'positive': score['pos'],
            'neutral': score['neu'],
            'negative': score['neg']      
        })
    with open(f'analysisResult/{fileName}', 'w') as file:
        json.dump(result, file, indent=4)

if __name__ == '__main__':
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    filesToRead = os.listdir('./data')
    for fileName in filesToRead:
        tweets = []
        print(fileName)
        with open(f"data/{fileName}", encoding='utf-8') as file:
            tweets = json.load(file)
        analyzeArrayOfTweets(tweets=tweets, fileName=fileName)
        

