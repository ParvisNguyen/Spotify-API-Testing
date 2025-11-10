from tabulate import tabulate

class ConsoleView:
    """Handles all text and table display for the user."""
    
    @staticmethod
    def display_artist_info(artist_data):
        print(f"\nArtist: {artist_data['name']}")
        print(f"Followers: {artist_data['followers']}")
        print(f"Genres: {', '.join(artist_data['genres']) if artist_data['genres'] else 'No genres available'}")
        print(f"Popularity: {artist_data['popularity']}/100")
        print("\nTop Tracks:")
        print(tabulate(artist_data['tracks'], headers=['Track', 'Album', 'Popularity'], tablefmt='pretty'))

    @staticmethod
    def display_history(history):
        print("\nRecent Searches:")
        for record in history:
            print(f"{record[1]} (Searched on {record[2]})")

    @staticmethod
    def no_artist_found(query):
        print(f"No artist found for query: '{query}'.")
