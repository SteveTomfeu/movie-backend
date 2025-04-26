# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %%
#Tester la récupération de quelques films
movies = db.query(Movie).limit(10).all()
for movie in movies:
    print(f" ID : {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")
else:
    print("No movies found.")
# %%
#Récupérer les films du genre Action
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()
for movie in action_movies:
    print(f" ID : {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
#Tester la récupération des évaluations
ratings = db.query(Rating).limit(10).all()
for rating in ratings:
    print(rating.userId, rating.movieId, rating.timestamp)
# %%
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
    .limit(5)
    .all()
)

print(high_rated_movies)

for title, rating in high_rated_movies:
    print(title, rating)
# %%
#Tester la récupération de quelques tags associés aux films
tags = db.query(Tag).limit(5).all()
for tag in tags:
    print(tag.movieId, tag.timestamp, tag.tag)
# %%
#Tester la classe link
links = db.query(Link).limit(5).all()

for link in links:
    print(link.movieId, link.imdbId, link.tmdbId)
# %%
db.close()
# %%
