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
