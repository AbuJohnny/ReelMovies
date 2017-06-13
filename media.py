class Movie():
    """Movie class

    Attributes:
        poster_image_url (str): Url of poster image
        title (str): Title of the movie
        trailer_youtube_url (str): Url of Youtube trailer
    """

    def __init__ (self, title, poster_image_url, trailer_youtube_url):
        """Instantiate a Movie object

        Args:
            title (str): Title of the Movie
            poster_image_url (str): Url of poster image
            trailer_youtube_url (str): Url of Youtube trailer
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
