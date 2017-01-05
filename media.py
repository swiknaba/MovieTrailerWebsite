import webbrowser

class Video():
    """Video: defining general properties for any videomaterial

    expected arguments: 2
        movie_title -- Title of the movie [text]
        movie_storyline -- short movie description [text]

    Inherits from: -/-
    Parent to: Movie

    Functions: -/-
    """
    def __init__(self, movie_title, movie_storyline):
        self.title = movie_title
        self.storyline = movie_storyline


class Movie(Video):
    """Movie: defines properties for movies and seasons of a serie

    expected arguments: 5
        movie_title -- Title of the movie resp. season [text]
        movie_duration -- Duration of movie/season in min. [integer]
        movie_storyline -- short movie description [text]
        poster_image -- image of the official movie poster [link]
        trailer_youtube -- official YouTube Trailer [link]

    Inherits from: Video
    Parent to: -/-

    Functions: -/-
    """
    def __init__(self, movie_title, movie_duration, movie_storyline,
                 poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_storyline)
        self.duration = movie_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube