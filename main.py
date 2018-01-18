import os
from collections import Counter

import httplib2
import time

import search
import comment_threads
import playlist
import channels
from apiclient.errors import HttpError
import sniffing
import user_radar
import videoCategory
import video
import activities
from googleapiclient.discovery import build


def get_authenticated_service():
    #create an class instance Youtube
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    return youtube



DEVELOPER_KEY = 'AIzaSyCDDfCQc7FX1yoX-JUYIpZJUluDx_uP7Y0' #Place here your key!
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
#videos,channel,playlist=search.youtube_search('J.-Ph. Rameau: «Les Surprises de')#query, max_results
while True:
    try:
        #Auth
        youtube=get_authenticated_service()
        CategoryYoutube=videoCategory.get_playlist_items(youtube) #Category list from Youtube
        break
    except (httplib2.ServerNotFoundError,TimeoutError) as e:
        print(e)
        time.sleep(10)

if os.path.exists("data"):
    print("Each_day")
    sniffing.each_day(youtube,CategoryYoutube)
else:
    os.mkdir("data")
    sniffing.start(youtube,CategoryYoutube)



#a=activities.get_last_activity(youtube,'UCr9oFpE-kIu7MNjKx_aR8dQ')

