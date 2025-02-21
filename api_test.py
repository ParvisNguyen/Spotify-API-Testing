import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="aeb9b9d5a28b4807b52c8df5d3d1cb83",
                                                           client_secret="4c2d792c20ea4786a384ea0f22453a04"))

# Example: Search for an artist
result = sp.search(q="The Weeknd", type="artist")

# Extract and display artist info
artist = result['artists']['items'][0]
print(f"Artist: {artist['name']}")
print(f"Followers: {artist['followers']['total']}")
print(f"Genres: {', '.join(artist['genres'])}")
print(f"Popularity: {artist['popularity']}/100")
