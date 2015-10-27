import time
from datetime import date

import fresh_tomatoes
import media

"""Create a gallery of movie trailers.

Creates and populates a list of pre-set movies and passes this list to 
fresh_tomatoes.py to dynamically generate a webpage gallery and opens
the web browser to this gallery.
"""

# Reference: http://www.imdb.com/title/tt0114709/
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio",
    date(1995, 11, 22),
    "G",
    81,
    92)

# Reference: http://www.imdb.com/title/tt0499549/
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    date(2009, 12, 18),
    "PG-13",
    162,
    83)

# Reference: http://www.imdb.com/title/tt2294629/
frozen = media.Movie(
    "Frozen",
    "A young woman gets the cold shoulder from her sister.",
    ("https://upload.wikimedia.org/wikipedia/en/0/05/"
        "Frozen_%282013_film%29_poster.jpg"),
    "https://www.youtube.com/watch?v=TbQm5doF_Uc",
    date(2013, 11, 27),
    "PG",
    102,
    74)

# Reference: http://www.imdb.com/title/tt0087332/
ghostbusters = media.Movie(
    "Ghostbusters",
    ("Three entrepreneurs start an innovative small business and tangle "
        "with the EPA."),
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png",
    "https://www.youtube.com/watch?v=vntAEVjPBzQ",
    date(1984, 6, 8),
    "PG",
    105,
    67)

# Reference: http://www.imdb.com/title/tt1663662/
pacific_rim = media.Movie(
    "Pacific Rim",
    ("A young woman restores an old classic ride and teams up with "
        "a grieving man to push back the new tenants."),
    ("https://upload.wikimedia.org/wikipedia/en/f/"
        "f3/Pacific_Rim_FilmPoster.jpeg"),
    "https://www.youtube.com/watch?v=5guMumPFBag",
    date(2013, 7, 12),
    "PG-13",
    131,
    64)

# Reference: http://www.imdb.com/title/tt1454468/
gravity = media.Movie(
    "Gravity",
    ("After a few fender benders, a doctor confronts her grief over "
        "her daughter's death as she hitches several rides around the world."),
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
    "https://www.youtube.com/watch?v=OiTiKOy59o4",
    date(2013, 10, 4),
    "PG-13",
    91,
    96)

# Create and populate list of movies
movie_list = [toy_story, avatar, frozen, ghostbusters, pacific_rim, gravity]

# Pass list of movies to fresh_tomatoes to generate gallery webpage
# and call default web browser to display it.
fresh_tomatoes.open_movies_page(movie_list)
