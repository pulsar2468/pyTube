# Call the API's commentThreads.list method to list the existing comments.
#output:[publishedAt,author,text,likeCount,authorChannelId])
def get_comments(youtube, video_id, channel_id=None):
    comment_list=[]
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        channelId=channel_id,
        textFormat="plainText",
        maxResults="100",
    ).execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        publishedAt= comment["snippet"]["publishedAt"]
        likeCount=comment["snippet"]["likeCount"]
        authorChannelId=comment["snippet"]["authorChannelId"]["value"]
        text = comment["snippet"]["textDisplay"]
        comment_list.append([publishedAt,author,text,likeCount,authorChannelId])


    while ('nextPageToken' in response):
        nextPageToken = response.get('nextPageToken')
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults="100",
            pageToken=nextPageToken
        ).execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            publishedAt= comment["snippet"]["publishedAt"]
            likeCount=comment["snippet"]["likeCount"]
            authorChannelId=comment["snippet"]["authorChannelId"]["value"]
            text = comment["snippet"]["textDisplay"]
            comment_list.append([publishedAt,author,text,likeCount,authorChannelId])
    return comment_list




