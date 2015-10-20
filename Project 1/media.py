import webbrowser

class Movie(object):
    """Creates movies with title, image, and trailer.

    Attributes:
        movie_title: A string containing the title of the movies
        poster_image: An url string to the poster image
        trailer_youtube: An url string to the youtube trailer
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens webbrowser and shows youtube trailer."""
        webbrowser.open(self.trailer_youtube_url)
