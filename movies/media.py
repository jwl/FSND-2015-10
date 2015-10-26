import webbrowser

class Movie(object):

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
            release_date, mpaa_rating, running_time, metascore):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.mpaa_rating = mpaa_rating
        self.running_time = running_time # in minutes
        self.metascore = metascore # Metacritic score as defined on Metacritic.com

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
