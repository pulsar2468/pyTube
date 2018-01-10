#Output:[title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
def get_playlist_items(youtube, id_videos,videoCategory):
    lang=None
    tags=None
    contentRating=None
    response = youtube.videos().list(
        id=id_videos,
        maxResults="50",
        part='snippet,contentDetails'
    ).execute()
    if response["items"]: 
        item=response["items"][0]
        title = item["snippet"]["title"]
        if title != "Deleted video" and title != "Private video" and title:
            if "lang" in item.keys():
                lang=item["snippet"]["defaultLanguage"]
            contentDetails=item["contentDetails"]
            if "contentRating" in contentDetails.keys():
                contentRating=contentDetails["contentRating"] # I wanted this field (violent content and other)
            category=item["snippet"]["categoryId"]
            #convert idCategory to nameCategory
            for i in videoCategory:
                if i[0] == category:
                    category=i[1]
                    break

            if "tags" in item.keys():
                tags=item["snippet"]["tags"]
            description = item["snippet"]["description"]
            videoPublishedAt = item["snippet"]["publishedAt"]

            return [title, description, videoPublishedAt,category,lang,tags,contentDetails,contentRating]
        else:
            return False
    else:
        return False
