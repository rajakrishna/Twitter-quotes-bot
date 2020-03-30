from PIL import Image, ImageDraw, ImageFont
import requests
import random

def quoteImg():
  file = open("./quotes/data.txt","r")
  lines = file.readlines() 
  i  = random.randint(0,len(lines)-1)

  #variables for image size
  x1 = 1024 
  y1 = 512
  #my quote
  sentence = lines[i]
  #choose a font
  fnt = ImageFont.truetype('./font/Abel.ttf', 40)
  # color is the backgroundColor of the Image
  img = Image.new('RGB', (x1, y1), color = (0,0,0))
  d = ImageDraw.Draw(img)
  #find the average size of the letter
  sum = 0
  for letter in sentence:
    sum += d.textsize(letter, font=fnt)[0]
  average_length_of_letter = sum/len(sentence)
  #find the number of letters to be put on each line
  number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
  incrementer = 0
  fresh_sentence = ''
  #add some line breaks
  for letter in sentence:
    if(letter == '-'):
      fresh_sentence += '\n\n' + letter
    elif(incrementer < number_of_letters_for_each_line):
      fresh_sentence += letter
    else:
      if(letter == ' '):
        fresh_sentence += '\n'
        incrementer = 0
      else:
        fresh_sentence += letter
    incrementer+=1
  #render the text in the center of the box
  dim = d.textsize(fresh_sentence, font=fnt)
  x2 = dim[0]
  y2 = dim[1]
  qx = (x1/2 - x2/2)
  qy = (y1/2-y2/2)
  # fill is the text color
  d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255, 255, 255))
  img.save('images/quote.png')
  
quoteImg()