from entertainment_center.media import Movie
import json
from entertainment_center import fresh_tomatoes

json_path = "data/movies.json"

movies = []

try:
    # Parse json data into Movie instances
    json_file = open(json_path)
    movies_json = json.load(json_file)
    json_file.close()

    for movie in movies_json['movies']:
        movies.append(Movie(
                movie['title'],
                movie['poster_image_url'],
                movie['trailer_youtube_url']
            ))

except IOError:
    print 'Error while trying to parse json data'

fresh_tomatoes.open_movies_page(movies)
