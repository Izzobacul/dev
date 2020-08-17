from spotipy import util, Spotify
from sys import argv

if len(argv)<4:
    print("Format: username playlist_id new_playlist_name")
    exit()
username = argv[1]
playlist_id = argv[2]
new_playlist_name = argv[3]

token = util.prompt_for_user_token(username=username,
                                   scope='playlist-read-private playlist-modify-private',
                                   client_id='c67fe2b4ced04e43a714fb85a610c07c',
                                   client_secret='82520b5e87d249749c249f6c216d83ba',
                                   redirect_uri='http://localhost/')

sp = Spotify(auth=token)
tracks = sp.playlist_tracks(playlist_id)
sp.user_playlist_create(username, new_playlist_name, public=False)

playlist = sp.user_playlists(username, limit=1)['items'][0]['id']

songs = []
for t in tracks['items']:
    songs.append(t['track']['uri'])

sp.user_playlist_add_tracks(username, playlist, songs)