# -*- coding: utf-8 -*-

import webbrowser


# 电影类
class Movie:
    # 有参构造函数
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
