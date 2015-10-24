import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
        "A story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
        "A marine on an alien planet.",
        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

frozen = media.Movie("Frozen",
        "A young woman gets the cold shoulder from her sister.",
        "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
        "https://www.youtube.com/watch?v=TbQm5doF_Uc")

ghostbusters = media.Movie("Ghostbusters",
        "A few Columbia University scientists start their own small business and tangle with the EPA.",
        "https://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png",
        "https://www.youtube.com/watch?v=vntAEVjPBzQ")

pacific_rim = media.Movie("Pacific Rim",
        "A young woman restores an old classic ride and teams up with a grieving man to push back the new tenants.",
        "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
        "https://www.youtube.com/watch?v=5guMumPFBag")

gravity = media.Movie("Gravity",
        "After a few fender benders, a doctor confronts her grief over daughter's death as she hitches several rides around the world.",
        "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
        "https://www.youtube.com/watch?v=OiTiKOy59o4")

movie_list = [toy_story, avatar, frozen, ghostbusters, pacific_rim, gravity]

fresh_tomatoes.open_movies_page(movie_list)
