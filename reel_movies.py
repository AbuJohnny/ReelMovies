from media import Movie
import fresh_tomatoes
import json


def get_movies_from_json(json_file_path):
    """Parses JSON File into a list of Movie objects

    Args:
        json_file_path (str): relative path to the JSON data file

    Returns:
        list: A list of Movie Objects, None if error parsing JSON
    """

    movies = []

    try:
        json_file = open(json_file_path)
        movies_json = json.load(json_file)
        json_file.close()

        # Parse json data into Movie instances and add them to the movies list
        for movie in movies_json['movies']:
            movies.append(Movie(
                    movie['title'],
                    movie['poster_image_url'],
                    movie['trailer_youtube_url']
                ))

    except IOError:
        print 'Error while trying to parse JSON data: File "' +\
            + json_file_path +\
            '" could not be opened'
        return None

    except ValueError:
        print 'Error while trying to parse JSON data: Invalid JSON'
        return None

    finally:
        return movies


if __name__ == "__main__":
    json_file_path = "data/movies.json"
    movies = get_movies_from_json(json_file_path)

    # Do not create and open the webpage if no movies are parsed
    if type(movies) is list:
        fresh_tomatoes.open_movies_page(movies)
