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

api = tweepy.API(auth)
api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True


def tweet_to_supporters(lang, lat, long, ref_id):
    blob = tweepy.Cursor(api.search,
                         q='#vhacks OR #migrants OR #refugees',
                         lang=lang,
                         geocode='{lat},{long},20km'.format(
                             lat=lat, long=long)).items()

    tweet_list = []

    for tweet in blob:
        tweet_list.append(tweet._json)

    # Sample for random 25 tweets because cog services are limited
    sample = random.sample(tweet_list, 25)

    documents = {'documents': []}

    for tweet in sample:
        documents['documents'].append(
            {'id': tweet['id'], 'language': tweet['lang'],
             'text': tweet['text']})

    # pp.pprint(documents)

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()['documents']

    id_score = sorted(sentiments, key=lambda k: k['score'], reverse=True)

    top_scores = id_score[:5]

    handles = []

    for element in top_scores:
        for tweet in sample:
            if tweet['id_str'] == element['id']:
                handles.append(tweet['user']['screen_name'])

    for handle in handles:
        api.update_status("@." + handle + '. You\'ve expressed an interest in '
                                          'helping refugees. We\'ve specially '
                                          'identified you as someone that '
                                          'could make a difference. Someone '
                                          'in your local area needs you. Text '
                                          '+447480619900 with reference code *'
                          + str(ref_id))
        time.sleep(1)

    pp.pprint(handles)


while True:
    ref_id += 1
    time.sleep(1)
    messages = client.messages.list()
    if messages[0].direction == 'inbound':
        text_to = messages[0].from_
        hi_text = messages[0].body.strip().split()[0]
        ref_lang = translator.detect(hi_text).lang

        translated_hi_msg = translator.translate(hi_msg, dest=ref_lang)
        hi_msg_command = twilio_command.format(
            account_sid=account_sid,
            auth_token=auth_token,
            text_to=text_to,
            content=translated_hi_msg.text)
        os.system(hi_msg_command)

        while True:
            time.sleep(5)
            new_msg = client.messages.list()[0]
            prev_msg = client.messages.list()[1]
            if new_msg.direction == 'inbound' \
                    and prev_msg.direction == 'outbound-api':
                break

        first_name = new_msg.body.strip().split()[0]
        translated_help_msg = translator.translate(
            help_msg.format(first_name=first_name), dest=ref_lang)
        help_msg_command = twilio_command.format(
            account_sid=account_sid,
            auth_token=auth_token,
            text_to=text_to,
            content=translated_help_msg.text)
        os.system(help_msg_command)

        while True:
            time.sleep(5)
            new_msg = client.messages.list()[0]
            prev_msg = client.messages.list()[1]
            if new_msg.direction == 'inbound' \
                    and prev_msg.direction == 'outbound-api':
                break
        request = translator.translate(new_msg.body, dest=ENGLISH)

        translated_location_msg = translator.translate(
            location_msg, dest=ref_lang)
        location_msg_command = twilio_command.format(
            account_sid=account_sid,
            auth_token=auth_token,
            text_to=text_to,
            content=translated_location_msg.text)
        os.system(location_msg_command)

        while True:
            time.sleep(5)
            new_msg = client.messages.list()[0]
            prev_msg = client.messages.list()[1]
            if new_msg.direction == 'inbound' \
                    and prev_msg.direction == 'outbound-api':
                num_msgs = len(client.messages.list())
                break

        geolocator = Nominatim()
        location = geolocator.geocode(new_msg.body, timeout=1000000)
        lat, long = location.latitude, location.longitude

        target_lang = 'en'
        meet_keywords = REQUEST_KEYWORDS_LANGUAGE.intersection(
            request.text.split())
        if len(meet_keywords) != 0:
            target_lang = ref_lang
        tweet_to_supporters(target_lang, lat, long, ref_id)

        translated_confirm_msg = translator.translate(
            confirm_msg, dest=ref_lang)
        confirm_msg_command = twilio_command.format(
            account_sid=account_sid,
            auth_token=auth_token,
            text_to=text_to,
            content=translated_confirm_msg.text)
        os.system(confirm_msg_command)

        while True:

            while True:
                time.sleep(5)
                msg_count = len(client.messages.list())
                sup_msg = client.messages.list()[0]
                prev_msg = client.messages.list()[1]

                if sup_msg.direction == 'inbound' \
                        and prev_msg.direction == 'outbound-api' \
                        and msg_count > num_msgs + 1:
                    break

            sup_number = sup_msg.from_
            ref_number = text_to

            translated_sup_msg = translator.translate(
                sup_msg.body, dest=ref_lang)
            sup_to_ref_msg_command = twilio_command.format(
                account_sid=account_sid,
                auth_token=auth_token,
                text_to=ref_number,
                content=translated_sup_msg.text)
            os.system(sup_to_ref_msg_command)

            if sup_msg.body == 'END':
                break

            while True:
                time.sleep(5)
                ref_msg = client.messages.list()[0]
                prev_msg = client.messages.list()[1]
                if ref_msg.direction == 'inbound' \
                        and prev_msg.direction == 'outbound-api':
                    break

            translated_ref_msg = translator.translate(
                ref_msg.body, dest=ENGLISH)
            ref_to_sup_msg_command = twilio_command.format(
                account_sid=account_sid,
                auth_token=auth_token,
                text_to=sup_number,
                content=translated_ref_msg.text)
            os.system(ref_to_sup_msg_command)

            if ref_msg.body == 'END':
                break
