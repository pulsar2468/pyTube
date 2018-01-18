# Output:title, description, id_video, videoPublishedAt, like_data
def get_playlist_items(youtube, id_playlist):
    list_item = []
    while True:
        try:
            response = youtube.playlistItems().list(
                playlistId=id_playlist,
                maxResults="50",
                part='snippet,contentDetails'
            ).execute()
            if response:
                if 'error' in response.keys():
                    print("Playlist not found")
                    return list_item
                for item in response["items"]:
                    title = item["snippet"]["title"]
                    if title != "Deleted video" and title != "Private video":
                        description = item["snippet"]["description"]
                        like_data = item["snippet"]["publishedAt"]
                        videoPublishedAt = item["contentDetails"]["videoPublishedAt"]
                        id_video = item["contentDetails"]["videoId"]
                        list_item.append([title, description, id_video, videoPublishedAt, like_data])

                while ('nextPageToken' in response):
                    nextPageToken = response.get('nextPageToken')
                    response = youtube.playlistItems().list(
                        playlistId=id_playlist,
                        maxResults="50",
                        part='snippet,contentDetails',
                        pageToken=nextPageToken
                    ).execute()
                    if response:
                        if 'error' in response.keys():
                            print("Playlist not found")
                            return list_item
                        for item in response["items"]:
                            title = item["snippet"]["title"]
                            if title != "Deleted video" and title != "Private video":  # otherwise i cannot get videoPublishedAt and other info
                                description = item["snippet"]["description"]
                                like_data = item["snippet"]["publishedAt"]
                                videoPublishedAt = item["contentDetails"]["videoPublishedAt"]
                                id_video = item["contentDetails"]["videoId"]
                                list_item.append([title, description, id_video, videoPublishedAt, like_data])

                return list_item
        except Exception as e:
            print("Error",e)

def get_new_items(youtube, id_playlist, last_datetime):
    list_item = []
    response = youtube.playlistItems().list(
        playlistId=id_playlist,
        maxResults="25",
        part='snippet,contentDetails'
    ).execute()
    if response:
        for item in response["items"]:
            title = item["snippet"]["title"]
            if title != "Deleted video" and title != "Private video":
                like_data = item["snippet"]["publishedAt"]
                if like_data > last_datetime:
                    print("New video")
                    description = item["snippet"]["description"]
                    videoPublishedAt = item["contentDetails"]["videoPublishedAt"]
                    id_video = item["contentDetails"]["videoId"]
                    list_item.append([title, description, id_video, videoPublishedAt, like_data])
                else:
                    print("Nothing changed")
                    return list_item

        while ('nextPageToken' in response):
            nextPageToken = response.get('nextPageToken')
            response = youtube.playlistItems().list(
                playlistId=id_playlist,
                maxResults="25",
                part='snippet,contentDetails',
                pageToken=nextPageToken
            ).execute()
            for item in response["items"]:
                like_data = item["snippet"]["publishedAt"]
                print(like_data, last_datetime)
                if like_data > last_datetime:
                    print("New video")
                    description = item["snippet"]["description"]
                    videoPublishedAt = item["contentDetails"]["videoPublishedAt"]
                    id_video = item["contentDetails"]["videoId"]
                    list_item.append([title, description, id_video, videoPublishedAt, like_data])
                else:
                    return list_item


    return list_item
