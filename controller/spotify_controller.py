import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tabulate import tabulate
import os
from dotenv import load_dotenv
from model.database import DatabaseConnection

load_dotenv()

class SpotifyController:
    # Handles artist search and Spotify API communication.
    def __init__(self):
        # Initialize Spotify client
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
        ))
        # Connect to the database
        self.db = DatabaseConnection()

    def search_artist(self, artist_name):
        # Search an artist and fetch top tracks.
        result = self.sp.search(q=artist_name, type="artist")
        if result['artists']['items']:
            artist = result['artists']['items'][0]
            artist_id = artist['id']
            artist_name = artist['name']
            followers = artist['followers']['total']
            genres = artist['genres']
            popularity = artist['popularity']
            top_tracks = self.sp.artist_top_tracks(artist_id)['tracks']

            # Store search in DB
            self.db.insert_artist(artist_name)

            # Build table of top tracks
            track_data = [[t['name'], t['album']['name'], t['popularity']] for t in top_tracks]

            # Return data to view
            return {
                "name": artist_name,
                "followers": followers,
                "genres": genres,
                "popularity": popularity,
                "tracks": track_data
            }
        else:
            return None

    def get_search_history(self):
        # Return the most recent artist searches.
        return self.db.fetch_history()
