
import json
import http.client
import re
from config import api_key, hashtag, dictonnary

# connection a la base de données local ou server

class Instagram_api():
    """
        in this class we will establish the connection to the instagram api
    """

    def __init__(self, api):
        self.key = api
        self.conn = None            # the connection event
        self.connection = True      # make an endpoit to check if connection established or not 
        self.data = {}              # the data used to manipulate the collection
        self.save_data = []         # the data to save in database

    """
        set the call function to the api with the right hashtag search
    """
    def __call__(self):
        self.conn = http.client.HTTPSConnection("instagram39.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': self.key,
            'x-rapidapi-host':  "instagram39.p.rapidapi.com"
            }
        self.conn.request("GET", "/getMediaByHashtag?tag_name="+ hashtag, headers=headers)
        res = self.conn.getresponse()
        data = res.read()
        # Load API response into a Python dictionary object, encoded as utf-8 string
        self.data = json.loads(data.decode("utf-8"))
        if (len(self.data) == 1):
            print ("error : ", self.data["message"])
            self.connection = False


    """
        extract the data needed to save in the database
        * extract the short code to search for the comments
        * extract the image needed
        * extract the text of the image
        * get the comments of the media
        * get the tags
    """
    def get_column_data(self):
        if (self.connection):
            # Loop through dictionary keys to access each Instagram Post
            posts = self.data["data"]["edges"]
            id = 0
            for item in posts:
                id += 1
                tags, text = self.get_hashtags_text(item)

                 # the trimed text
                text_trim = self.trim_text(text)        

                # encode the tags
                for elem in tags:
                    elem = elem.encode('utf-8')
                
                numLikes = item['node']['edge_liked_by']['count']
                shortcode = item['node']['shortcode']
                img_profile = item['node']['thumbnail_src']
                nb_comments = item['node']['edge_media_to_comment']['count']

                # verify if the the text refere to the pernality's death
                if (self.bags_of_words(text_trim) != -1):
                    if (nb_comments > 0):
                        comments = self.get_post_comment(shortcode)
                    else:
                        comments = []

                    self.save_data.append({
                        "shortcode": shortcode,
                        "text": text.decode("utf-8"),
                        "likes": numLikes,
                        "img_url": img_profile,
                        "comments": comments,
                    })

    """
        this function is used to trim the text and remove all the : 
        - remove all single characters
        - Substituting multiple spaces with single space
        - Removing prefixed 'b'
        - Remove all the special characters
    """
    def trim_text(self, text):
        doc = ""
        # remove all the special characters
        for character in text:
            if chr(character).isalnum() or chr(character) == ' ':
                doc += chr(character)
        # remove all single characters
        doc = re.sub(r'\s+[a-zA-Z]\s+', ' ', doc)
        # Substituting multiple spaces with single space
        doc = re.sub(r'\s+', ' ', doc, flags=re.I)
        # Removing prefixed 'b'
        doc = re.sub(r'^b\s+', '', doc)# Converting to Lowercase
        doc = doc.lower()
        return (doc)


    """
        this function is just to trime the text and get the different hashtags
    """
    def get_hashtags_text(self, item):
        text = item['node']['edge_media_to_caption']['edges'][0]['node']['text'].replace('#','\n#')
        tags = text.split("\n")
        return (tags, text.encode('utf-8')) 


    """
        this function is used to get the comments on the media selected
        - make the call to the api
        - search with the short code selected
    """
    def get_post_comment(self, shortcode):
        headers = {
            'x-rapidapi-key': self.key,
            'x-rapidapi-host':  "instagram39.p.rapidapi.com"
            }
        self.conn.request("GET", "/getMediaComments?short_code=" + shortcode, headers=headers)

        res = self.conn.getresponse()
        des = res.read()
        data = json.loads(des.decode("utf-8"))
        result = []
        # Load API response into a Python dictionary object, encoded as utf-8 string
        if (len(data) == 1):
            print ("error while trying to get comments : ", data["message"], "skip...")
        else:
            comments = data['data']["edges"]
            for element in comments:
                result.append(element['node']['text'])
        return (result)

    """
        check if the text is refering to death of our character
    """
    def bags_of_words(self, text):
        for element in dictonnary:
            if (str(text).find(element)):
                return (True)
        return (False)

    


