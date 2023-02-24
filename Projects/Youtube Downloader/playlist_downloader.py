from pytube import Playlist

lista_playlist = open("./playlists.txt", "r").readlines()


for playlist in lista_playlist:
    linha = playlist.strip()
    lista = linha.split(";")
    url = lista[1]
    
    youtube_playlist = Playlist(url)
    print(f"[Playlist] - {lista[0]}")
    for video in youtube_playlist.videos:
        if  not video.age_restricted:
            video.streams.get_lowest_resolution().download(f"./Músicas/{lista[0]}")
            print(f"\tVídeo baixado: {video.title}")
print("Download realizado com sucesso.")