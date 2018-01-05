def get_playlist_items(youtube,id_playlist):
    response = youtube.playlistItems().list(
        playlistId=id_playlist,
        maxResults="100",
        part='snippet,contentDetails'
    ).execute()
    print(response)