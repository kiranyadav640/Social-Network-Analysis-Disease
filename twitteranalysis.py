# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from TwitterSearch import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt
import networkx as nx
import json
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['dengue']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'consumer id',
        consumer_secret = 'consumer secret key',
        access_token = 'access token',
        access_token_secret = 'access token secret key'
     )
    
    
    
    i=0
    tp=0
    
    p=0
    n=0
    ng=0

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        blob = TextBlob(tweet['text'])
        i += 1
        tp =  (blob.sentiment.polarity)
        if tp > 0:
            p += 1
            
        elif tp == 0:
            n += 1
        elif tp < 0:
            ng += 1
        if i == 10000:
            break
    
   
    
    
    labels = 'Positive', 'Negative'
    sizes = [p, ng]
    colors = ['yellowgreen', 'lightskyblue' ]
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    

        

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

