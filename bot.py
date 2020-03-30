import tweepy
import os
import glob
from PIL import Image
import quoteImg



# Authenticate to Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Twitter Status
# api.update_status("Hello World")

# Twitter Image
def bot():
    api.update_with_media('./images/quote.png')
    print("sucess")


quoteImg.quoteImg()
bot()






    






