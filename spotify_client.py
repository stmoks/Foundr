# Using the Spotipy API that links to the popular music streaming site Spotify
# Completed with the help of Max Tingle @ Medium, 
# https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

import pandas as pd
from spotipy import SpotifyClientCredentials,oauth2,Spotify,util
import sys,os

#export SPOTIPY_REDIRECT_URI=""
# authenticating my credentials
cid = "702f99bae6f5489da997f6c86663956b"
secret_id = "08d83f6fe0a0483799fb4891477e757b"
#set SPOTIPY_REDIRECT_URI=Enter your redirect URL here
client_credentials_manager = SpotifyClientCredentials(client_id = cid,client_secret = secret_id)
sp = Spotify(client_credentials_manager=client_credentials_manager)

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'


## playing music using my virtual assistant
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

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



