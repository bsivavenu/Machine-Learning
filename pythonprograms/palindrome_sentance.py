# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:49:55 2018

@author: HP
"""

#import urllib.request 
##filename = 2

#urllib.request.urlretrieve(url, filename)

#import pandas as pd
#df = pd.read_csv('c:/users/HP/Desktop/2.csv')
#print(df.head())
#
#import requests
#image_url = 'http://numerologystars.com/wp-content/uploads/2011/12/number-2-2.jpg'
#img_data = requests.get(image_url).content
#with open('image_name.jpg', 'wb') as handler:
#    handler.write(img_data)
#Import Python Imaging Library (PIL) 
#import Image 
from PIL import Image
import numpy as np

#pilimg = Image.open('2.jpg')
#pilimg.save(“pil.jpg”)

img = Image.open( '2.jpg')
img.load()
data = np.asarray( img, dtype="int32" )
print(data)

# Convert PIL image to numpy array 
#arr = numpy.array(pilimg)

#Convert numpy array to PIL image 
#pilimg = Image.fromarray(arr)