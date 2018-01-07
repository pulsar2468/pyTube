#Output:title, description, id_video, videoPublishedAt, like_data
def get_playlist_items(youtube, id_playlist):
    list_item = []
    response = youtube.playlistItems().list(
        playlistId=id_playlist,
        maxResults="50",
        part='snippet,contentDetails'
    ).execute()
    if response:
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
            for item in response["items"]:
                title = item["snippet"]["title"]
                if title != "Deleted video" and title != "Private video": # otherwise i cannot get videoPublishedAt and other info
                    description = item["snippet"]["description"]
                    like_data = item["snippet"]["publishedAt"]
                    videoPublishedAt = item["contentDetails"]["videoPublishedAt"]
                    id_video = item["contentDetails"]["videoId"]
                    list_item.append([title, description, id_video, videoPublishedAt, like_data])

        return list_item
