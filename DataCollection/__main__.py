# import tweepy
import json
import os
import snscrape.modules.twitter as sntwitter
from datetime import datetime
# from dotenv import load_dotenv
# import tweepy.auth
from QueryConstructor import QueryConstructor


def getDataFromTwitterSnscrape(query, startTime, endTime, fileName):
    result = []
    for tweet in sntwitter.TwitterSearchScraper(f'asdf').get_items():
        result.append({
            'text': tweet.content,
            'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
            'username': tweet.user.username,
            'retweet_count': tweet.retweetCount,
            'like_count': tweet.likeCount,
    })
    with open(fileName, 'w') as f:
        json.dump(result, f, indent=4)
    return result

def getDataFromTwitter(client, query, startTime, endTime, maxResult, fileName):
    result = []
    try:
        response = client.search_all_tweets(
            query=query,
            end_time=endTime,
            start_time=startTime,
            max_results=maxResult,
            expansions=['referenced_tweets.id'],
            tweet_fields=[
                'id', 'text', 'attachments', 'author_id', 'geo'
                'created_at', 'organic_metrics', 'public_metrics',
                'promoted_metrics', 'referenced_tweets', 'lang','context_annotations',
            ],
            user_fields=[
                'author_id', 'in_reply_to_user_id'
            ]
        )
        for tweet in response.data:
            result.append(tweet)

    except tweepy.TweepyException as e:
        print(e)
    finally:
        with open(fileName, 'w') as f:
            json.dump(result, f, indent=4)
        return result

if __name__ == '__main__':
    # load_dotenv()
    # token = os.getenv('BEARER_TOKEN')
    # customerKey = os.getenv('API_KEY')
    # customerSec = os.getenv('API_SECRET_KEY')
    # accessToken = os.getenv('ACCESS_TOKEN')
    # accessSec = os.getenv('ACCESS_TOKEN_SECRET')
    # client = tweepy.Client(bearer_token=token, consumer_key=customerKey, consumer_secret=customerSec, access_token=accessToken, access_token_secret=accessSec)

    hashTagsToUseEverton = ['#Everton','#EFC', '#EvertonFC', '#Toffees', '#FFP', '#EvertonFFP', '#EvertonBan', '#FinancialFairPlay', '#FFPBreach']
    keyWordsToUseEverton = ['Everton FFP charges', 'Everton financial fair play', 'Everton fine', 'Everton FFP penalty', 'Everton punishment', 'FFP charges Everton', 'Everton point deduction', 'Everton investigation', 'Everton financial breach', 'Premier League Everton FFP', 'Everton sanctions']
    handleToUseEverton  = ['@Everton', '@EvertonNewsFeed', '@LivEchoEFC', '@EFC_FanAdvisory', '@EFCfanzome', '@efc_engagement', '@fansofefc']
    
    hashTagsToUseManchester = ['#MCFC', '#ManCity', '#ManchesterCity', '#Cityzens', '#FFP', '#ManCityFFP', '#FFPBreach', '#FinancialFairPlay', '#ManCityFine']
    keyWordsToUseManchester = ['Man City FFP charges', 'Man City financial fair play', 'Man City FFP breach', 'Manchester City fine', 'Man City FFP penalty', 'Manchester City punishment', 'FFP charges Manchester City', 'Man City point deduction', 'Manchester City investigation', 'Man City financial breach', 'Premier League Man City FFP', 'Manchester City sanctions']
    handleToUseManchester   = ['@ManCity', '@City_Xtra', '@ManCityMEN', '@City_Chief']

    hashTagsToUseAdhoc = ['#FFP', '#FinancialFairPlay', '#UEFAFFP', '#PremierLeagueFFP', '#FFPRegulations']
    keyWordsToUseAdhoc = ['FFP breach', 'financial fair play rules', 'financial fair play rules', 'financial fair play rules', 'FFP investigation', 'FFP fine', 'FFP point deduction', 'FFP compliance', 'UEFA financial fair play']



    Everton = QueryConstructor(handleToUseEverton, keyWordsToUseEverton, handleToUseEverton)
    ManCity = QueryConstructor(handleToUseManchester, keyWordsToUseManchester, handleToUseManchester)
    Adhoc   = QueryConstructor(hashTagsToUseAdhoc, keyWordsToUseAdhoc, [])

    # startTime = '2025-08-15T00:00:00Z'
    # endTime = '2025-08-25T00:00:00Z'

    # evertonTweets=  getDataFromTwitter(query=Everton.createQuery(),client=client, endTime=endTime, startTime=startTime, maxResult=10, fileName='data/everton_tweets.json')
    # manCityTweets=  getDataFromTwitter(query=ManCity.createQuery(),client=client, endTime=endTime, startTime=startTime, maxResult=10, fileName='data/man_city_tweets.json')
    # adhocTweets  =  getDataFromTwitter(query=Adhoc.createQuery(),  client=client, endTime=endTime, startTime=startTime, maxResult=10, fileName='data/adhoc_tweets.json')

    startTime = '2025-08-15T00:00:00Z'
    endTime = '2025-08-25T00:00:00Z'

    evertonTweets=  getDataFromTwitterSnscrape(query="", endTime=endTime, startTime=startTime, fileName='data/everton_tweets.json')
    manCityTweets=  getDataFromTwitterSnscrape(query="", endTime=endTime, startTime=startTime, fileName='data/man_city_tweets.json')
    adhocTweets  =  getDataFromTwitterSnscrape(query="",   endTime=endTime, startTime=startTime, fileName='data/adhoc_tweets.json')


    print("Data Collected")