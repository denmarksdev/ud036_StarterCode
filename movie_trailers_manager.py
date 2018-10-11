import media
import marks_movie_trailers


def create_movie_trailers():
    matrix_reloaded = media.Movie("Matrix reloaded",
                                  "A story a hacker to save the world",
                                  ("https://m.media-amazon.com/images/M" 
                                  + "/MV5BMGZjNGQ4MmItM2MwZS00YWE1LThhND" 
                                  + "QtN2RhY2QwNTk4YmVmXkEyXkFqcGdeQXVyO" 
                                  + "DA1NjQ0OTY@._V1_.jpg"),
                                  "https://www.youtube.com/watch?v=kYzz" 
                                  "0FSgpSU")

    gladiator = media.Movie("Gladiator",
                            "A Roman General fight your honor as gladiator",
                            ("https://upload.wikimedia.org/wikipedia/en/" 
                             + "thumb/8/8d/Gladiator_ver1.jpg/220px-Gladia" 
                             + "tor_ver1.jpg"),
                            "https://www.youtube.com/watch?v=uvbavW31adA")

    indiana_jones = media.Movie("Indiana Jones",
                                "Treasure hunters and pulp action heroes",
                                ("https://images-na.ssl-images-amazon.com/" 
                                 + "images/I/61F7bV5N9xL.jpg"),
                                "https://www.youtube.com/watch?v=HqOSLZl9GUo")

    pursuit_happyness = media.Movie("The Pursuit of Happyness",
                                    "Gardner becomes obstinate for the " 
                                     "survival and sustenanc e of his family",
                                     ("https://upload.wikimedia.org/wikipedia" 
                                     + "/pt/thumb/1/1e/The_Pursuit_of_Happynes" 
                                     + "s.jpg/200px-The_Pursuit_of_Happyness.jpg"),
                                    "https://www.youtube.com/watch" +
                                    "?v=89Kq8SDyvfg")

    who_am_i = media.Movie("Jackie Chan's Who Am I?",
                           "Guy lost memory, but have mission to complet",
                           ("https://resizing.flixster.com/xs7Ac2TA-eaZalo" 
                           + "45XkmDBaZZHc=/206x305/v1.bTsxMjE4NDgzNTtqOzE3" 
                           + "ODI2OzEyMDA7Mjg0OzQwNQ"),
                           "https://www.youtube.com/watch?v=Gdx55aI-BLw")

    terminator2 = media.Movie("Terminator 2",
                              "The protection came the future",
                              ("https://http2.mlstatic.com/poster-cartaz-ext" 
                               + "erminador-do-futuro-2-terminator-40x60cm-D_NQ" 
                               + "_NP_686685-MLB25905408285_082017-O.jpg"),
                              "https://www.youtube.com/watch?v=lwSysg9o7wE")

    return [matrix_reloaded, gladiator, indiana_jones,
            pursuit_happyness, who_am_i, terminator2]


# Populate site with data
movies = create_movie_trailers()

marks_movie_trailers.open_movies_page(movies)
