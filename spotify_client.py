# Using the Spotipy API that links to the popular music streaming site Spotify
# Completed with the help of Max Tingle @ Medium, 
# https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

import pandas as pd
from spotipy import SpotifyClientCredentials,oauth2,Spotify


# credentials
cid = "702f99bae6f5489da997f6c86663956b"
secret_id = "08d83f6fe0a0483799fb4891477e757b"
client_credentials_manager = SpotifyClientCredentials(client_id = cid,client_secret = secret_id)
sp = Spotify(client_credentials_manager =client_credentials_manager)


# setting up the dataframe
artist_name = []
track_name = []
popularity = []
track_id = []
country = []

for i in range(0,30,1):
    track_results = sp.search(q = "year:2020-2021", type = "track", limit = 30)
    for j,tr in enumerate(track_results["tracks"]["items"]):
        artist_name.append(tr["artists"][0]["name"])
        track_name.append(tr["name"])
        track_id.append(tr["id"])
        popularity.append(tr["popularity"])

#some info about artists
for i in range(0,30,1):
    artist_results = sp.search(q = "artist:The Weeknd", type = "artist", limit = 30)
    for j,tr in enumerate(artist_results["artist"]["items"]):
        artist_name.append(tr["artists"][0]["name"])
        country.append(tr["country"])


track_dataframe = pd.DataFrame({"artist_name":artist_name,"track_name":track_name,
"track_id":track_id,"popularity":popularity},{"country":country})

# the most popular tracks
new_df = track_dataframe.sort_values("popularity",ascending=False)
new_df = new_df.drop_duplicates("track_id")
print(new_df.head(20))