import os
from flask import Flask, jsonify, abort, request
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.route('/')
    def get_home():
        greeting = "Welcome to the movie app!"
        return greeting

    @app.route("/actors", methods=["GET"])
    def get_actors():
        actors = Actor.query.all()
        actor_list = []
        for actor in actors:
            actor_list.append(actor.format())

        if actors is None:
            abort(404)

        return jsonify(actor_list)

    @app.route("/movies", methods=["GET"])
    def get_movies():
        movies = Movie.query.all()
        movie_list = []
        for movie in movies:
            movie_list.append(movie.format())

        if movies is None:
            abort(404)
            
        return jsonify(movie_list)

    @app.route("/actors/<actor_id>", methods=["DELETE"])
    @requires_auth('delete:actor')
    def delete_actor(actor_id):
        try:
            Actor.query.get(actor_id).delete()            
            return jsonify({
                'success': True,
            })
        except:
            abort(422)

    @app.route("/movies/<movie_id>", methods=["DELETE"])
    @requires_auth('delete:movie')
    def delete_movie(movie_id):
        try:
            Movie.query.get(movie_id).delete()            
            return jsonify({
                'success': True,
            })
        except:
            abort(422)

    @app.route("/actors", methods=["POST"])
    @requires_auth('post:actor')
    def add_actor():
        body = request.get_json()
        try:
            Actor(
                name = body.get('name'),
                age = body.get('age'),
                gender = body.get('gender'),
            ).insert()

            return jsonify({
                'success': True,
            })
        except:
            abort(422)


    @app.route("/movies", methods=["POST"])
    @requires_auth('post:movie')
    def add_movie():
        body = request.get_json()
        try:
            Movie(
                title = body.get('title'),
                release_year = body.get('release_year'),
            ).insert()

            return jsonify({
                'success': True,
            })
        except:
            abort(422)


    @app.route("/actors/<actor_id>", methods=["PATCH"])
    @requires_auth('patch:actor')
    def update_actor(actor_id):
        body = request.get_json()
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)
            if "name" in body:
                actor.name = body.get("name")
            if "age" in body:
                actor.age = int(body.get("age"))
            if "gender" in body:
                actor.gender = body.get("gender")
            actor.update()
            return jsonify({"success": True,})
        except:
            abort(400)


    @app.route("/movies/<movie_id>", methods=["PATCH"])
    @requires_auth('patch:movie')
    def update_movie(movie_id):
        body = request.get_json()
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)
            if "title" in body:
                movie.title = body.get("title")
            if "release_year" in body:
                movie.release_year = int(body.get("release_year"))
            movie.update()
            return jsonify({"success": True,})
        except:
            abort(400)


    # Error Handling

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            'error': 400,
            'success': False,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(403)
    def not_found(error):
        return jsonify({
            'error': 403,
            'success': False,
            'message': 'Not Authenticated'
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 404,
            'success': False,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'error': 422,
            'success': False,
            'message': 'Unprocessable'
        }), 422

    return app

    app = create_app()

if __name__ == '__main__':
    app.run()
