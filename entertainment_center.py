# coding=utf-8
"""
Routine to define the movies to show and to launch the website.
"""


import media
import fresh_tomatoes as fp

# Create some movies examples to show on website
avatar = media.Movie('https://www.youtube.com/watch?v=5PSNL1qE6VY',
                     'Avatar',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@'
                     '._V1_UX182_CR0,0,182,268_AL_.jpg')

birth_nation = media.Movie('https://www.youtube.com/watch?v=i18z1EQCoyg',
                           'The Birth of a Nation',
                           'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5MjI3NzQxMl5BMl5BanBnXkFtZTgwMTUwN'
                           'jYyOTE@._V1_UX182_CR0,0,182,268_AL_.jpg')

girl_on_train = media.Movie('https://www.youtube.com/watch?v=y5yk-HGqKmM',
                            'The Girl on the Train',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwNDU4NTQwMl5BMl5BanBnXkFtZTgwMzQ2M'
                            'jIwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg')

middle_school = media.Movie('https://www.youtube.com/watch?v=XQtjPUyS6ZY',
                            'Middle School: The Worst Years of My Life',
                            'https://images-na.ssl-images-amazon.com/images/M/MV5BNjQzMTczNjI0Ml5BMl5BanBnXkFtZTgwODY5M'
                            'TY5OTE@._V1_UX182_CR0,0,182,268_AL_.jpg')

underworld = media.Movie('https://www.youtube.com/watch?v=r6FxROAHJH4',
                         'Underworld: Blood Wars',
                         'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNjk2MzY3Nl5BMl5BanBnXkFtZTgwMjg1N'
                         'jEwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg')

# Create a list with movies to show on website
movies = [avatar, birth_nation, girl_on_train, middle_school, underworld]

# Launch the website to see movie's trailers
fp.open_movies_page(movies)
