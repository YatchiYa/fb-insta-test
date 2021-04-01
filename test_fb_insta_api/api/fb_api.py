

"""
import json
import http.client
import re
import facebook
from config import api_key, hashtag, dictonnary

# connection a la base de données local ou server

class Facebook_api():

        # in this class we will establish the connection to the Facebook_api api


    def __init__(self, token):
        self.token = token
        self.conn = None            # the connection event
        self.connection = True      # make an endpoit to check if connection established or not 
        self.data = {}              # the data used to manipulate the collection
        self.save_data = []         # the data to save in database

 
        # set the call function to the api with the right hashtag search 
    def __call__(self):
        self.conn = facebook.GraphAPI(access_token=self.token)

"""