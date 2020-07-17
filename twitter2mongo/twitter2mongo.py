#!/usr/bin/env python3

import  urllib, tweepy
from pymongo import MongoClient
import logging

logging.basicConfig(filename='twitter2mongo.log',level=logging.INFO)
logging.info('---------START SESSION----------')
try:
    # Connect to MongoDB
    pw = ""
    cluster = MongoClient('mongodb+srv://:'+ pw + '')    
    db = cluster["trends"]
    collection_berlin = db["berlin"]
    collection_stuttgart = db["stuttgart"]
    logging.info('connected to db')

    # Authenticate to TwitterAPI
    auth = tweepy.OAuthHandler("", "")
    auth.set_access_token("", "") 
    api = tweepy.API(auth)
    logging.info('authenticated to TwitterAPI')

    # Do API calls
    data_berlin = api.trends_place(638242)
    logging.info('Trends for Berlin'+ str(data_berlin))
    data_stuttgart = api.trends_place(698064)
    logging.info('Trends for Stuttgart'+ str(data_stuttgart))
    logging.info('called TwitterAPI')

    # Insert into MongoDB
    collection_berlin.insert_many(data_berlin)
    collection_stuttgart.insert_many(data_stuttgart)
    logging.info('inserted data to MongoDB')

    # Finally close connection to MongoDB
    cluster.close()
    logging.info('closed connection')
except Exception as e:
    print('Exception'+ str(e))
    logging.info('Exception'+ str(e))

logging.info('---------FINISH SESSION---------')
