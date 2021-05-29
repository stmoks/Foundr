# Using the Spotipy API that links to the popular music streaming site Spotify
# Completed with the help of Max Tingle @ Medium, 
# https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

import pandas as pd
from spotipy import SpotifyClientCredentials,oauth2,Spotify,util
import sys,os,webbrowser

import spotipy

# authenticating my credentials
cid = "702f99bae6f5489da997f6c86663956b"
secret_id = "08d83f6fe0a0483799fb4891477e757b"
redirect_url = "https://www.google.com/"
username = "j389o9xb4nnxfn1fvoftubvst"
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

client_credentials_manager = SpotifyClientCredentials(client_id = cid,client_secret = secret_id)


## playing music using my virtual assistant
try:
    token = util.prompt_for_user_token(username, scope,cid,secret_id,redirect_url)
except (AttributeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope,cid,secret_id,redirect_url)

sp = Spotify(client_credentials_manager=client_credentials_manager,auth=token)
print(sp.devices)


# setting up the dataframe
artist_name = []
track_name = []
popularity = []
track_id = []


# for i in range(0,20,1):
#     track_results = sp.search(q = "year:2020-2021", type = "track", limit = 30)

#     for j,tr in enumerate(track_results["tracks"]["items"]):
#         artist_name.append(tr["artists"][0]["name"])
#         track_name.append(tr["name"])
#         track_id.append(tr["id"])
#         popularity.append(tr["popularity"])
    

#some info about the artists
# for i in range(0,15,1):
#     artist_results = sp.search(q = "artist:The Weeknd", type = "artist", limit = 30)

#     for j,art in enumerate(artist_results["artists"]["items"]):
#         artist_name.append(art["name"])
#         popularity.append(art["popularity"])
#         track_name.append("")
#         track_id.append("")


artist_search = "The Weeknd"
artist_results = sp.search(q = f"artist:{artist_search}", type = "artist", limit = 1)

album_search = "Can't Feel My Face"
album_results = sp.search(q = f"track:{album_search}", type = "album", limit = 1)

track_search = "Can't Feel My Face"
track_results = sp.search(q = f"track:{track_search}", type = "track", limit = 1)

track_dataframe = pd.DataFrame({"artist_name":artist_name,"track_name":track_name,
"track_id":track_id,"popularity":popularity})

# the most popular tracks
new_df = track_dataframe.sort_values("popularity",ascending=False)
new_df = new_df.drop_duplicates("track_id")
print(new_df.head(20))

# Print artist details
searchResults = sp.search(artist_search,1,0,"artist")
artist = searchResults['artists']['items'][0]
print(artist['name'])

# webbrowser.open(artist['images'][0]['url'])
artistID = artist['id']

# Extract data from album
album_results = sp.artist_albums(artistID)
album_results = album_results['items']


 # Album details
trackURIs = []
trackArt = []
i = 0

devices = sp.devices()
print(devices)
deviceID = devices['devices'][0]['id']

for item in album_results:
    print("ALBUM: " + item['name'])
    albumID = item['id']
    albumArt = item['images'][0]['url']

    # Extract track data
    trackResults = sp.album_tracks(albumID)
    trackResults = trackResults['items']

    for item in trackResults:
        print(str(i) + ": " + item['name'])
        trackURIs.append(item['uri'])
        trackArt.append(albumArt)
        i += 1
    print()

# See album art
while True:
    trackSelectionList = []
    trackSelectionList.append(trackURIs[int(181)])
    sp.start_playback(deviceID, None, trackSelectionList)
    webbrowser.open(trackArt[0])




