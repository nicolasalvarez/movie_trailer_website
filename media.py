# coding=utf-8
"""
Movie class definition
"""


class Movie(object):
    """
    Movie class with the following attributes:
    - trailer_youtube_url: trailer youtube url
    - title: movie title
    - poster_image_url: poster image url
    - trailer_youtube_id: trailer youtube id
    """
    def __init__(self, trailer_youtube_url, title, poster_image_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = None
