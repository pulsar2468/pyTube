import httplib2
import time
from googleapiclient.discovery import build
import itertools
import video
import comment_threads
import videoCategory
import fresh_and_clean
import lemmatizer_content

def get_authenticated_service():
    #create an class instance Youtube
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    return youtube

def create_doc(video_info,all_comments):
    # video_info_format:[title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
    # comments_format:[publishedAt,author,text,likeCount,authorChannelId])
    fusion_comments = list(itertools.chain.from_iterable([i[2]] for i in all_comments))
    #TODO remember of the tags and contentDetails!
    doc=[video_info[0],video_info[1],video_info[3],video_info[5]]+fusion_comments
    doc_clean_unmerge=fresh_and_clean.clean_text(doc,grammarList)
    doc_clean=list(itertools.chain.from_iterable(doc_clean_unmerge))
    return lemmatizer_content.lemmatizer_words(doc_clean)


DEVELOPER_KEY = 'AIzaSyCDDfCQc7FX1yoX-JUYIpZJUluDx_uP7Y0' #Place here your key!
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
#videos,channel,playlist=search.youtube_search('J.-Ph. Rameau: «Les Surprises de')#query, max_results
while True:
    try:
        #Auth
        youtube=get_authenticated_service()
        CategoryYoutube=videoCategory.get_playlist_items(youtube) #Category list from Youtube
        grammarList=fresh_and_clean.load_stop_word("long_stop_word")
        break
    except httplib2.ServerNotFoundError as e:
        print(e)
        time.sleep(10)

video_info=video.get_playlist_items(youtube,'xj6PWqyuW-U',CategoryYoutube)
all_comments=comment_threads.get_comments(youtube,'xj6PWqyuW-U')
doc_video=create_doc(video_info,all_comments) #create doc from video info plus all commments about it
print(doc_video)

