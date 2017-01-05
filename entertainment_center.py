import media
import fresh_tomatoes
import fresh_tomatoes_series

toy_story = media.Movie(
    "Toy Story",  # Movie Title
    81,  # Movie duration in minutes
    "A story of a boy and his toys, computer animated movie",  # Description
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # Poster
    "https://youtu.be/KYz2wyBy3kc")  # Trailer

avatar = media.Movie(
    "Avatar",
    161,
    "A marine on an alien planet, basically Pocahontas as science fiction",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY")

lucky_number_slevin = media.Movie(
    "Lucky Number Slevin",
    110,
    "A guy at the wrong place at the wrong time meets The Boss and The Rabbi",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/Lucky_Number_Slevin_Theater_Poster.JPG",  # NOQA
    "https://youtu.be/mGQmSCQrKKQ")

ai_artificial_intelligence = media.Movie(
    "A.I. Artificial Intelligence",
    146,
    "Robot David pursuing happiness fails receiving love from his human mother",
    "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
    "https://youtu.be/_19pRsZRiz4")

who_am_i = media.Movie(
    "Who Am I",
    105,
    "A small Berlin based hacker team challenging BND, world class hackers, as"
    " well as the cyber mafia",
    "https://upload.wikimedia.org/wikipedia/en/5/5c/Who_am_I_movie_poster.jpg",
    "https://youtu.be/5vnjheCqRIs")

i_saw_the_devil = media.Movie(
    "I Saw the Devil",
    141,
    "The lines between good and evil fall away in this diabolically twisted"
    " game of cat and mouse",
    "https://upload.wikimedia.org/wikipedia/en/6/69/Isawthedevil.jpg",
    "https://youtu.be/xwWgp1bqVwE")

the_sea_inside = media.Movie(
    "The Sea Inside",
    125,
    "Quadriplegic Ramon fights 28 years lying in his bed to end his life",
    "https://upload.wikimedia.org/wikipedia/en/0/04/Mar_adentro_poster.jpg",
    "https://youtu.be/dVRnG1MddAM")

secret_walter_mitty_2013 = media.Movie(
    "The Secret Life of Walter Mitty (2013)",
    114,
    "Daydreamer Walter gently takes on a personal journey to achieve greatness",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg",  # NOQA
    "https://youtu.be/HddkucqSzSM")

breaking_bad_season1 = media.Movie(
    "Breaking Bad: Season 1",
    336,
    "7 Episodes, Released 2008<br>Chemistry teacher diagnosed with cancer turns"
    " to a life of crime",
    "https://upload.wikimedia.org/wikipedia/en/6/61/BreakingBadS1DVD.jpg",
    "https://youtu.be/HhesaQXLuRY")

breaking_bad_season2 = media.Movie(
    "Breaking Bad: Season 2",
    611,
    "13 Episodes, Released 2009",
    "https://upload.wikimedia.org/wikipedia/en/e/e0/BreakingBadS2DVD.jpg",
    "https://youtu.be/I-8914DuyhY")

breaking_bad_season3 = media.Movie(
    "Breaking Bad: Season 3",
    611,
    "13 Episodes, Released 2010",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Breaking_Bad_season_3_DVD.png",  # NOQA
    "https://youtu.be/ZK2IQ3LbLYk")

breaking_bad_season4 = media.Movie(
    "Breaking Bad: Season 4",
    611,
    "13 Episodes, Released 2011",
    "https://upload.wikimedia.org/wikipedia/en/b/bd/Breaking_Bad_season_four_DVD.jpg",  # NOQA
    "https://youtu.be/WcUmzPcQEJo")

breaking_bad_season5 = media.Movie(
    "Breaking Bad: Season 5",
    752,
    "2 x 8 Episodes, Released 2012 and 2013",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Breaking_Bad_season_five_part_i_and_ii_dvd.png",  # NOQA
    "https://youtu.be/_b8SQ3H1BO4")

westworld_season1 = media.Movie(
    "Westworld: Season 1",
    740,
    "10 Episodes, Released 2016<br>Future amusement park populated with"
    " androids powered by AI - what could go wrong?",
    "http://assets1.ignimgs.com/2016/09/01/1274080mktpawestworlds1keyartpov1jpg-42cbc1_765w.jpg",  # NOQA
    "https://youtu.be/0zZcBv0gPK0")

westworld_season2 = media.Movie(
    "Westworld: Season 2",
    0,
    "10 Episodes, Expected 2018",
    "http://assets2.ignimgs.com/2016/09/28/fin01westworld1shtjpg-f9a6f7_765w.jpg",  # NOQA
    "https://youtu.be/6RorQW1SdK8")

# put all movies in one list
movies = [toy_story, avatar, lucky_number_slevin, ai_artificial_intelligence,
          who_am_i, i_saw_the_devil, the_sea_inside, secret_walter_mitty_2013,
          breaking_bad_season1, breaking_bad_season2, breaking_bad_season3,
          breaking_bad_season4, breaking_bad_season5, westworld_season1,
          westworld_season2]

# hand over movies to its fresh_tomatoes html generator, call generator
fresh_tomatoes.open_movies_page(movies)