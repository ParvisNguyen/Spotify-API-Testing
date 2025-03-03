import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
# Import tabulate to display data in a table format
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()

# Authentication Setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Searches for an artist in a query
# q is the search query
# type is the type of item to search for
search_query = "Porter Robinson"
result = sp.search(q=search_query, type="artist")

#Checks if there is an artist found
if result['artists']['items']:
    
# Extract artist info
# result is a dictionary returned by sp.search()
# 'artist' contains artists found in the search query
# 'items' contains the list of artists found
# [0] is used to get the first artist in the list
    artist = result['artists']['items'][0]
    artist_id = artist['id']
    artist_name = artist['name']    
    followers = artist['followers']['total']
    genres = artist['genres']
    popularity = artist['popularity']

# Extract and display artist info
    print(f"\n🎵 Artist: {artist_name}")
    print(f"👥 Followers: {followers}")
# Checks if genres is not empty, if it is then it will print 'No genres available'
    print(f"🎼 Genre(s): {', '.join(genres) if genres else 'No genres available'}")
    print(f"🔥 Popularity: {popularity}/100")

# Takes top tracks of artist
    top_tracks = sp.artist_top_tracks(artist_id)['tracks']

# Extract track details
    track_data=[]
    for track in top_tracks:
        track_data.append([track['name'], track['album']['name'], track['popularity']])
    
    print("\n🎵 Top Tracks:")
    print(tabulate(track_data, headers=['Track', 'Album', 'Popularity'], tablefmt='pretty'))

else:
    print (f"No Aritst found for the query: '{serach_query}'.")