
import os
import requests
import json
import http.client
import pandas
import facebook

from db.database import *
from api.insta_api import *
from api.fb_api import *
from config import api_key, db_url

def main():
    # establish the connection to database
    db = database(db_url)
    # set the call function to connect the database
    db()
    
    #establish the connection to instagram api
    insta_api = Instagram_api(api_key['insta_api_key'])
    insta_api()
    insta_api.get_column_data()

    # save the data
    for elem in insta_api.save_data:
        db.save_to_database(elem)
    
    # just to test to retrieve the data
    #data = db.get_data_from_database()
    #print (data["likes"])
    """
    fb_api = Facebook_api(api_key["token_fb"])
    fb_api()
    """

# main call
if __name__ == '__main__':
    print ("preprocessing started...")
    main()
