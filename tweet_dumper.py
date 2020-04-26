#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "lq6ryVXnIKRyQGmFi5uEqMLPJ"
consumer_secret = "EylINJoPTDL9ij808SaOkT5yGr4aLf44wpu2IjXziTYrv13DBc"
access_key = "993250657003024384-zGc044KDDizKs7WAXrswgeGFjkttlln"
access_secret = "Tar8yaS1jdeysG0dG1YIoBDgk7mypBuJ63KTbH4UQ3PHc"


def get_all_tweets(screen_name):
        #Twitter only allows access to a users most recent 3240 tweets with this method
        
        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        
        #initialize a list to hold all the tweepy Tweets
        alltweets = []  
        
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
                print ("getting tweets before %s" % (oldest))
                
                #all subsiquent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
                
                #save most recent tweets
                alltweets.extend(new_tweets)
                
                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1
                
                print( "...%s tweets downloaded so far" % (len(alltweets)))
        
        #transform the tweepy tweets into a 2D array that will populate the csv 
        outtweets = [[tweet.text] for tweet in alltweets]
        
        #write the csv  
        writer = open('corpus.txt', "a", encoding='utf-8')

        for tweet in outtweets:
                tweet_text = str(tweet[0])


                
                if not tweet_text.startswith("RT"):
                        writer.write(tweet_text + "\n")

        print("done with " + screen_name) 
        pass


if __name__ == '__main__':
        #pass in the username of the account you want to download
        get_all_tweets("thatartsyfail")
"""
        get_all_tweets("virkenstock")
        get_all_tweets("seaofbitter")
        get_all_tweets("HeccHead")
        get_all_tweets("funkjockboy")
        get_all_tweets("UmExcuseMeMandi")
        get_all_tweets("bauhausdad")
        get_all_tweets("fountxin")
        get_all_tweets("scottioli")
        get_all_tweets("proteincat")
        get_all_tweets("_FortyTwo_")
        get_all_tweets("JulietteReeder4")
        get_all_tweets("coolguy6410")
        get_all_tweets("isabellaaaahhh")
        get_all_tweets("DoTheNeighNeigh")
        get_all_tweets("vehnti")
        get_all_tweets("dylabjoeb")
        """

