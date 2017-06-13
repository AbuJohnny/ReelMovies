from media import Movie
import fresh_tomatoes
import json

json_path = "data/movies.json"

movies = []

try:
    # Parse json data from file
    json_file = open(json_path)
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
    print 'Error while trying to parse json data'

fresh_tomatoes.open_movies_page(movies)
