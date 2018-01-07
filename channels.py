#output:id playlist liked video
def get_id_liked_playlist(youtube,id_channel):
    response = youtube.channels().list(
        id=id_channel,
        part='contentDetails',
    ).execute()
    id_playlist=response["items"][0]["contentDetails"]["relatedPlaylists"]
    if "likes" in id_playlist.keys():
        return id_playlist["likes"] # this is id Playlist of liked video
    else:
        return False

'''def get_user_information(youtube,id_channel):
    response = youtube.channels().list(
        id=id_channel,
        part='snippet,contentDetails',
    ).execute()
    print(response)
    exit()'''