import markovify
import tweepy
import time



#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Get raw text as string.
with open("corpus.txt", encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, reject_reg = r"@")
text_model.well_formed = True



while(True):
    tweet = text_model.make_short_sentence(280)
    print(tweet)
    api.update_status(tweet)

    time.sleep(3600)
    
