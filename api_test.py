import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

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
result = sp.search(q="Porter Robinson", type="artist")

# Extract artist info
# result is a dictionary returned by sp.search()
# 'artist' contains artists found in the search query
# 'items' contains the list of artists found
# [0] is used to get the first artist in the list
artist = result['artists']['items'][0]

artist_name = artist['name']
followers = artist['followers']['total']
genres = artist['genres']
popularity = artist['popularity']

# Extract and display artist info
print(f"Artist: {artist_name}")
print(f"Followers: {followers}")
# Checks if genres is not empty, if it is then it will print 'No genres available'
print(f"Genre(s): {', '.join(genres) if genres else 'No genres available'}")
print(f"Popularity: {popularity}/100")
