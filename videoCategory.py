def get_playlist_items(youtube):
    CategoryList=[]
    response = youtube.videoCategories().list(
        part='snippet',
        regionCode='US'
    ).execute()

    for item in response["items"]:
        CategoryId=item["id"]
        CategoryName=item["snippet"]["title"]
        CategoryList.append([CategoryId,CategoryName])

    return CategoryList