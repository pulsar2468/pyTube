import pickle
import datetime
import comment_threads
import channels
import playlist
import video
import os

def save_list(name, data):
        try:
            with open(name, 'wb') as f:
                # json.dump(list_followers,f)
                pickle.dump(data, f)
                f.close()
        except IOError:
            print('I/O error')
            exit('Exit')

def open_dataset(name):
    try:
        with open(name, 'rb') as f:
            l = pickle.load(f)
        f.close()
    except IOError:
        print('File not found!')
        exit('Exit')
    return l


def start(youtube,CategoryYoutube):
    videos_info=[]
    comment_list=comment_threads.get_comments(youtube,'6mTEpicRFwM') #Object,id_video
    print("Comment catched: ",len(comment_list))
    try:
        for i in comment_list:
            id_liked_video=channels.get_id_liked_playlist(youtube,i[4])
            if id_liked_video is not False:
                print("User: ",i[1]," Playlist Liked: ",id_liked_video," ChannelId: ",i[4])
                list_item=playlist.get_playlist_items(youtube,id_liked_video)
                #title, description, id_video, videoPublishedAt, like_data
                for j in list_item:
                    tmp = video.get_playlist_items(youtube,j[2],CategoryYoutube)
                    #Output:[title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
                    if tmp:
                        tmp.append(j[4])
                        tmp.append(id_liked_video)
                        videos_info.append(tmp)
                        #if user_radar.start_radar(Counter([j[3] for j in videos_info]), i[1],CategoryYoutube):
                        #print("Radar Chart created")
                os.makedirs("data/"+i[1])
                save_list("data/"+i[1]+'/'+str(datetime.date.today()),videos_info)
                videos_info.clear()
                tmp.clear()
    except Exception as e:
        print(e)

def last_file(directory):
    for (root, dirnames, files) in os.walk("data/"+directory):
        return files[len(files)-1]


def each_day(youtube,CategoryYoutube):
    flag=False
    today=datetime.date.today()
    #yesterday=str(datetime.date(today.year,today.month,today.day-1))
    for (root, dirnames, files) in os.walk("data/"):
        for name in dirnames:
            while True:
                try:
                    l_file=last_file(name)
                    if l_file and not os.path.exists("data/"+name+'/'+str(today)):
                        load_list=open_dataset("data/"+name+'/'+l_file)
                        print("Analyse user: ",name)
                        #for i in load_list:
                        list_item=playlist.get_new_items(youtube,load_list[0][9],load_list[0][8])
                        #title, description, id_video, videoPublishedAt, like_data
                        for j in list_item:
                            tmp = video.get_playlist_items(youtube,j[2],CategoryYoutube)
                            #Output:[title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
                            if tmp:
                                tmp.append(j[4])
                                tmp.append(load_list[9])
                                load_list.insert(0,tmp.copy())
                                tmp.clear()
                                flag=True
                                #if user_radar.start_radar(Counter([j[3] for j in videos_info]), i[1],CategoryYoutube):
                                #print("Radar Chart created")
                        if flag:
                            save_list("data/"+name+'/'+str(datetime.date.today()),load_list)
                            flag=False
                        break
                    else:
                        print("File: ",name," has been checked!")
                        break
                except Exception as e:
                    print(e)