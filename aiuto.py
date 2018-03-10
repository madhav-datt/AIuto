from twilio.rest import Client
from googletrans import Translator
import time
import os
from geopy.geocoders import Nominatim
import pprint
import random
import requests
import tweepy

ENGLISH = "en"
REQUEST_KEYWORDS_LANGUAGE = {
    "lonely", "companion", "talk", "meet", "alone", "companionship", "meeting",
    "conversation", "education", "discuss", "discussion"}

account_sid = "Twilio Account ID"
auth_token = "Twilio Authorization Token"
client = Client(account_sid, auth_token)
translator = Translator()
ref_id = 1000

twilio_command = r"""curl 'https://api.twilio.com/2010-04-01/Accounts/AC8b026e99c205a0b0bacd60bdf3c45337/Messages.json' -X POST \
--data-urlencode 'To={text_to}' \
--data-urlencode 'From=+447480619900' \
--data-urlencode 'Body={content}' \
-u {account_sid}:{auth_token}"""

hi_msg = "Hi, I am AIuto. What is your name?"
help_msg = "Thanks {first_name}! What could we help you with?"
location_msg = "Where are you located?"
confirm_msg = "Please wait - we are looking for someone who can help"

pp = pprint.PrettyPrinter(indent=4)

# Tweepy tokens
ACCESS_TOKEN = "Access Token"
ACCESS_SECRET = "Access Secret"
CONSUMER_KEY = "Consumer Key"
CONSUMER_SECRET = "Consumer Secret"

# MS Cognitive Service Tokens
subscription_key = "MS Subscription Key"
assert subscription_key

# REST Endpoint for Cog Servs
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)




