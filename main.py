from controller.spotify_controller import SpotifyController
from view.console_view import ConsoleView

def main():
    controller = SpotifyController()
    view = ConsoleView()

    while True:
        search_query = input("\nEnter an artist or type 'exit' to quit: ").strip()
        if search_query.lower() == 'exit':
            print("Goodbye! 👋")
            break

        artist_data = controller.search_artist(search_query)
        if artist_data:
            view.display_artist_info(artist_data)
            history = controller.get_search_history()
            view.display_history(history)
        else:
            view.no_artist_found(search_query)

if __name__ == "__main__":
    main()
