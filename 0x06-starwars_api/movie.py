import requests
import sys


def get_movie_characters(movie_id):
    # Define the base URL for the Star Wars API
    base_url = "https://swapi-api.alx-tools.com/api/films/"

    try:
        # Ensure movie_id is a valid integer
        movie_id = int(movie_id)
    except ValueError:
        print("Error: Movie ID must be a valid integer.")
        sys.exit(1)

    # Make a request to the API to get the movie information
    response = requests.get(base_url + str(movie_id))

    # Check if the request was successful
    if response.status_code == 200:
        movie_data = response.json()
        characters = movie_data.get("characters", [])

        if characters:
            for character_url in characters:
                # Get character information
                character_response = requests.get(character_url)
                if character_response.status_code == 200:
                    character_data = character_response.json()
                    character_name = character_data.get("name")
                    print(character_name)
                else:
                    print(
                        f"Failed to fetch character data for {character_url}")
        else:
            print("No characters found for this movie.")
    else:
        print("Failed to fetch movie data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_movie_characters(movie_id)
