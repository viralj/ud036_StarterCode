import fresh_tomatoes
import media

"""
Different Movie objects with the information passed in it.
"""
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")

x_men = media.Movie("X-Men: Apocalypse",
                    "After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjU1ODM1MzYxN15BMl5BanBnXkFtZTgwOTA4NDE2ODE@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=PfBVIHgQbYk")

"""
Movies list to store all Movie objects created above. This list will be passed in open_movies_page function to create
html page and open it in web browser to display information about movies.
"""

movies = [interstellar, inception, the_matrix, avatar, the_martian, x_men]

"""
Calling 'open_movies_page' function from 'fresh_tomatoes' to open movies page showing information passed in movies list.
"""
fresh_tomatoes.open_movies_page(movies)
