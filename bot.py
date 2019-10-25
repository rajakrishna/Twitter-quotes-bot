import tweepy
import os
import glob
from PIL import Image
import threading


# Authenticate to Twitter
auth = tweepy.OAuthHandler("fcQ5eOoOaOt0tlbcl75IIjPcO", "F4RQRQwOEnho0jEd3twlMoaXZRMYuNTMZCcMiDLe0kDFCGX4iS")
auth.set_access_token("1452342498-zQwz1agN6senzofP39s9Pf5aTflpVyGHs18EMBP", "E5yMy1NTSZdWFBXVglpdx8cSPJiHO658cxYIKOfzPO9yE")

# Create API object
api = tweepy.API(auth)

# Create a tweet
# api.update_status("Hello World")

images = glob.glob("images/*.png")


for image in images:
    imagePath = image
    # status = "Check out our new website"
    # api.update_with_media(imagePath, status)
    api.update_with_media(imagePath)
    print("sucess")










    






