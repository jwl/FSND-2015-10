import webbrowser


class Movie(object):
    """Contains all the relevant information about an individual movie.

        Args:
        movie_title (str): Title of movie.
        movie_storyline (str): One or two sentence story summary of movie.
        poster_image (str): URL for poster image for movie.
        trailer_youtube (str): URL for theatrical trailer for movie.
        release_date (date): Original theatrical release date for movie.
        mpaa_rating (int): MPAA rating
                running_time (int): Original theatrical running time in minutes
                metascore (int): Metacritic score as defined on Metacritic.com

        Attributes:
        title (str): Title of movie.
        storyline (str): One or two sentence story summary of movie.
        poster_image_url (str): URL for poster image for movie.
        trailer_youtube_url (str): URL for theatrical trailer for movie.
        release_date (date): Original theatrical release date for movie.
        mpaa_rating (int): MPAA rating
        running_time (int): Original theatrical running time in minutes
        metascore (int): Metacritic score as defined on Metacritic.com

    """

    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube,
            release_date, mpaa_rating, running_time, metascore):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.mpaa_rating = mpaa_rating
        self.running_time = running_time
        self.metascore = metascore

    def show_trailer(self):
        """Invoke webbrowser to open YouTube trailer in trailer_youtube_url"""
        webbrowser.open(self.trailer_youtube_url)
