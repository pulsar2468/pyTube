import httplib2
import time
from googleapiclient.discovery import build
import itertools
import video
import comment_threads
import videoCategory
import fresh_and_clean
import lemmatizer_content

def create_vocabulary(full_set):
    return list(set(itertools.chain.from_iterable(full_set)))


def alignment_terms(vocabulary, term_list, tf_list):
    alignment = [0]*len(vocabulary)
    for i in term_list:
        if i in vocabulary:
            index=vocabulary.index(i)
            alignment.insert(index, tf_list[term_list.index(i)]) #because two array are aligned
        else:
            alignment.insert(term_list.index(i),0)

    return alignment


def open_set(name):
    try:
        l = []
        with open(name, 'r') as f:
            l = ([i.rstrip('\n') for i in f.readline().split(',')])
        f.close()
        return l
    except IOError:
        # log_file("File developer key not found"+'\n')
        print('Target file not found! Create into target_list!')
        exit('Exit')


def tf_schema(doc_video):
    i=0
    tf_list = []
    replicated = []
    len_doc_video = len(doc_video)
    while i < len(doc_video):
        if doc_video[i] not in replicated:
            count = doc_video.count(doc_video[i])
            tf_list.append(count / len_doc_video)
            replicated.append(doc_video[i])
            i=i+1
        else:
            doc_video.pop(i)
    return tf_list

def get_authenticated_service():
    # create an class instance Youtube
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    return youtube


def create_doc(video_info, all_comments):
    # video_info_format:[title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
    # comments_format:[publishedAt,author,text,likeCount,authorChannelId])
    fusion_comments = list(itertools.chain.from_iterable([i[2]] for i in all_comments))
    # TODO remember of the tags and contentDetails!
    doc = [video_info[0], video_info[1], video_info[3], video_info[5]] + fusion_comments
    doc_clean_unmerge = fresh_and_clean.clean_text(doc, grammarList)
    doc_clean = list(itertools.chain.from_iterable(doc_clean_unmerge))
    return lemmatizer_content.lemmatizer_words(doc_clean)


DEVELOPER_KEY = 'AIzaSyCDDfCQc7FX1yoX-JUYIpZJUluDx_uP7Y0'  # Place here your key!
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
# videos,channel,playlist=search.youtube_search('J.-Ph. Rameau: «Les Surprises de')#query, max_results
while True:
    try:
        # Auth
        youtube = get_authenticated_service()
        CategoryYoutube = videoCategory.get_playlist_items(youtube)  # Category list from Youtube
        grammarList = fresh_and_clean.load_stop_word("long_stop_word")
        break
    except httplib2.ServerNotFoundError as e:
        print(e)
        time.sleep(10)

full_term_set = []
full_set_tf = []
items_id = open_set("labeled/space")

for video_id in items_id:
    video_info = video.get_playlist_items(youtube, video_id, CategoryYoutube)
    all_comments = comment_threads.get_comments(youtube, video_id)
    doc_video = create_doc(video_info, all_comments)  # create doc from video info plus all commments about it
    full_term_set.append(doc_video)
    full_set_tf.append(tf_schema(doc_video))

# create vocabulary of all documents..
vocabulary=create_vocabulary(full_term_set)

#i scroll the term list with to relative tf_list of video I get it..
#this is a way fundamental to alignment the term for each video_doc generated, it based to the words of all of video categories
for term_list,tf_list in zip(full_term_set,full_set_tf):
    tf_alignment=alignment_terms(vocabulary,term_list,tf_list)
