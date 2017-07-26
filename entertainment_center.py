import fresh_tomatoes
import media

"""
Different Movie objects with the information
passed in it. Storyline object and poster
image link object for each movies created
separately to follow PEP8 formatting guideline.
"""

interstellar_sl = "A team of explorers travel through " \
                  "a wormhole in space in an " \
                  "attempt to ensure humanity's survival."

interstellar_pi = "https://images-na.ssl-images-amazon.com" \
                  "/images/M/" \
                  "MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3Mj" \
                  "E@._V1_SY1000_CR0,0,640,1000_AL_.jpg"

interstellar = media.Movie("Interstellar",
                           interstellar_sl,
                           interstellar_pi,
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception_sl = "A thief, who steals corporate secrets through " \
               "use of dream-sharing technology, " \
               "is given the inverse task of planting " \
               "an idea into the mind of a CEO."

inception_pi = "https://images-na.ssl-images-amazon.com/" \
               "images/M/MV5BMjAxMzY3NjcxNF5BMl5Ba" \
               "nBnXkFtZTcwNTI5OTM0Mw@@." \
               "_V1_SY1000_CR0,0,675,1000_AL_.jpg"

inception = media.Movie("Inception",
                        inception_sl,
                        inception_pi,
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_matrix_sl = "A computer hacker learns from " \
                "mysterious rebels about the true " \
                "nature of his reality and his role " \
                "in the war against its controllers.",

the_matrix_pi = "https://images-na.ssl-images-amazon.com" \
                "/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVk" \
                "LWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyX" \
                "kFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0" \
                ",0,665,1000_AL_.jpg"

the_matrix = media.Movie("The Matrix",
                         the_matrix_sl,
                         the_matrix_pi,
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

avatar_sl = "A paraplegic marine dispatched to the " \
            "moon Pandora on a unique mission " \
            "becomes torn between following his " \
            "orders and protecting the world he feels is his home."

avatar_pi = "https://images-na.ssl-images-amazon.com" \
            "/images/M/MV5BMTYwOTEwNjAzMl5B" \
            "Ml5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg"

avatar = media.Movie("Avatar",
                     avatar_sl,
                     avatar_pi,
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_martian_sl = "An astronaut becomes stranded on " \
                 "Mars after his team assume him dead," \
                 " and must rely on his ingenuity to " \
                 "find a way to signal to Earth that he is alive."

the_martian_pi = "https://images-na.ssl-images-amazon.com" \
                 "/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXk" \
                 "FtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg"

the_martian = media.Movie("The Martian",
                          the_martian_sl,
                          the_martian_pi,
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")

x_men_sl = "After the re-emergence of the world's " \
           "first mutant, world-destroyer Apocalypse, " \
           "the X-Men must unite to defeat his extinction level plan."

x_men_pi = "https://images-na.ssl-images-amazon.com/" \
           "images/M/MV5BMjU1ODM1MzYxN15BMl5BanBnXk" \
           "FtZTgwOTA4NDE2ODE@._V1_SY1000_CR0,0,676,1000_AL_.jpg"

x_men = media.Movie("X-Men: Apocalypse",
                    x_men_sl,
                    x_men_pi,
                    "https://www.youtube.com/watch?v=PfBVIHgQbYk")

"""
Movies list to store all Movie objects created above.
This list will be passed in open_movies_page
function to create html page and open it in
web browser to display information about movies.
"""

movies = [interstellar, inception, the_matrix, avatar, the_martian, x_men]

"""
Calling 'open_movies_page' function from
'fresh_tomatoes' to open movies page showing
information passed in movies list.
"""
fresh_tomatoes.open_movies_page(movies)
