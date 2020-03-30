# Twitter Quotes Bot

Create Twitter Developer profile

# Authentication
Open bot.py and add the keys
```
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
```

# Pip
`pip install requirements.txt`

Run bot.py

## Change the size
quoteImg.py

x1 = width

y1 = height

Exmaple `x1=1024 y1=512`

## Change the background color
quoteImg.py

`img = Image.new('RGB', (x1, y1), color = (RGB Code))`

Example `color=(255,255,255)`

## Change the text color
quoteImg.py

`d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(RGB Code))`

Example `fill=(255,255,255)`

## Locations
The quotes are found in quotes/data.txt

Image background is created in quoteImg.py using Pillow 

## Result (Quote.png)
![Image_with_quote](/images/quote.png)
