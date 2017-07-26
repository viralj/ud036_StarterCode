class Movie():
    """
    Movie class to create data set of different movies
    and store their information.

    Attributes:
        title : To store information of movie title
        storyline : To store information of movie story line
        poster_image : To store information of movie poster image
        trailer_link : To store information of movie trailer link
    """

    def __init__(self, title, storyline, poster_image, trailer_link):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link
