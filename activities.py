#Output:title, description, id_video, videoPublishedAt, like_data
def get_last_activity(youtube, channel_id):
    list_item = []
    response = youtube.activities().list(
        channelId=channel_id,
        maxResults="50",
        part='snippet,contentDetails'
    ).execute()
    for item in response["items"]:
        type=item["snippet"]["type"]
        #print(type)
        if type == "like":
            title = item["snippet"]["title"]
            if title != "Deleted video" and title != "Private video":
                description = item["snippet"]["description"]
                like_data = item["snippet"]["publishedAt"]
                id_video = item["contentDetails"][type]["resourceId"]["videoId"]

        #elif type == "comment":
            #print(item["snippet"]["resourceId"])
                list_item.append([title, description, id_video, like_data,type])

    while ('nextPageToken' in response):
        nextPageToken = response.get('nextPageToken')
        response = youtube.activities().list(
            channelId=channel_id,
            maxResults="50",
            part='snippet,contentDetails',
            pageToken=nextPageToken
        ).execute()
        for item in response["items"]:
            type=item["snippet"]["type"]
            #print(type)
            if type == "like":
                title = item["snippet"]["title"]
                if title != "Deleted video" and title != "Private video":
                    description = item["snippet"]["description"]
                    like_data = item["snippet"]["publishedAt"]
                    id_video = item["contentDetails"][type]["resourceId"]["videoId"]
                    list_item.append([title, description, id_video, like_data,type])
    return list_item
