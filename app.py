from flask import Flask, redirect, render_template, request, abort


from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

app = Flask(__name__)

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)

@app.errorhandler(404)

@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    mname = request.form.get('name', type = str)
    dname = request.form.get('dname', type = str)
    rating = request.form.get('select', type = str)
    if mname is "" or dname is "" or rating is "":
        return render_template("404.html")
    else:
        int_rating = int(rating)
        movie_repository.create_movie(mname, dname, int_rating)
        return render_template('list_all_movies.html', get_all_movies=movie_repository.get_all_movies(), list_movies_active=True)


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    searchVal = request.args.get('moviesearch', None)
    searchResult = None
    
    for movie in movie_repository.get_all_movies():
        if movie.title == searchVal:
            searchResult = movie
    
    return render_template('search_movies.html', searchResult=searchResult, search_active=True)
