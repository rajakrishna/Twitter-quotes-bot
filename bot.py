import tweepy
import os
import glob
from PIL import Image
import quoteImg



# Authenticate to Twitter
auth = tweepy.OAuthHandler("fcQ5eOoOaOt0tlbcl75IIjPcO", "F4RQRQwOEnho0jEd3twlMoaXZRMYuNTMZCcMiDLe0kDFCGX4iS")
auth.set_access_token("1452342498-zQwz1agN6senzofP39s9Pf5aTflpVyGHs18EMBP", "E5yMy1NTSZdWFBXVglpdx8cSPJiHO658cxYIKOfzPO9yE")

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






    






