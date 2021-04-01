
from pymongo import MongoClient, errors
from datetime import datetime
import sys
from config import db_url

# connection a la base de données local ou server

class database():
    """
        in this class we will establish the connection to the data base
         - either to local database 
         - or to  server data that is defined in atlas mongoDB in Amazon cloud
    """

    def __init__(self, db_url):
        self.url = db_url
        self.db = None

    """
        call function to establish connection
    """
    def __call__(self):
        try:
            print ("database connected")
            self.db = MongoClient(self.url)
        except errors.ConnectionFailure:
            print ("Failed to connect to server {}".format(self.url))
            self.db = None

    """
        save data to database
        - set the database name and the collection name
    """
    def save_to_database(self, data):
        jc_data = self.db["jc_data"]
        table = jc_data["deaths_posts"]
        table.insert_one(data)
        print ("data loaded to database....")


    """
        function to get the all data from the database
    """
    def get_data_from_database(self):
        jc_data = self.db["jc_data"]
        table = jc_data["deaths_posts"]
        data = []
        for x in table.find():
            data.append(x)
        print ("data retrieved successfully....")
        return (data)

