import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

CASTING_DIRECTOR_JWT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllNelVsOHVvZXVQclFTTV9oWXJTSiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmkxazRyanBsNGd2dHVmLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzVjMjcyYTcyNDMyNzZkZTQ3ODZjZjYiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTY3MDQ3MDIwMCwiZXhwIjoxNjcwNTU2NjAwLCJhenAiOiJXUW9WYWFSbUlmQTV6RUE1T2N4NFFMM1hmT0xmblVsMCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.RMhuP23910Iy9OMlKcd6GCSNsk_tRWk4K5n31GWP9qBZxqNDxY6VjRZaTyJSRcy2DQEGuRUi1HX7sE_Dj9QuiZY6yAzAAhyAI8E5gohDgza9PCK45oSXpqUZFtJfoz0tyG_CpJNSemDP7ebh_OWMVgPVWfvW1hJa5IseUnOYkbD1r-ScbXbO61EMuOIvOdoIZSFy7LYm5aEEhErTvI5VZCA8tdBB9Q0OSoZjZ2uaNZNseyYSOxcwuoWREXmvnD2Zfhu1pbkKfzvgf-ve9S-KMatJJ8zL_RCzgnVMBjVFFgBto3tKSfbOhsRD9_CyGUjj4IhrvhlaVBt3TEwIY876aQ'
EXECUTIVE_PRODUCER_JWT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllNelVsOHVvZXVQclFTTV9oWXJTSiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmkxazRyanBsNGd2dHVmLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkxNWMxMTY1YTFhODJlZjUwZDAyM2IiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTY3MDQ3MDg2MiwiZXhwIjoxNjcwNTU3MjYyLCJhenAiOiJXUW9WYWFSbUlmQTV6RUE1T2N4NFFMM1hmT0xmblVsMCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.P1Nf6Yg43BGFKwwWVB_Mlnew9IDPrRK63-UekMMJEqsCMsZpnkdPnWGD86YYhRN2mMmaD6bYqfRs-WlnkgHqFkUD-5Hjluu3cvPGOYxTgVXNKftAibkVNMSy4-OtAHbzW9LSaTQvLPGtz-Qu1eP53numMIs9BaAgXBmbNoy5oNQYrjOdzWrTcC6mJg5qFxSZTxcYKatMHz5thIuGV4nX8of51b1hDezepYI27ZC57V7RRbtWOiKoG_Id74chcGwO5GjuAtN9Co1xelyR0d02QLFK4B0ZAQ_ToPLUiL46IkHyF-1IzVxkDQOdx3wsKVXolEnOWyq6WauGUpRw84WEuA'


class MovieAppTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movieapp_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        #self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_get_home(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_actors(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 200)

    def test_get_movies(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 200)

    def test_add_actor_producer(self):
        res = self.client().post(
            '/actors',
            headers={
                'Authorization': EXECUTIVE_PRODUCER_JWT,
                }, 
            json={
                'age': 43,
                'name': 'Chris Pratt',
                'gender': 'Male'
                }
            )
        self.assertEqual(res.status_code, 200)

    def test_add_actor_casting(self):
        res = self.client().post(
            '/actors', 
            headers={
                'Authorization': CASTING_DIRECTOR_JWT,
                },
            json={
                'age': 43,
                'name': 'Chris Pratt',
                'gender': 'Male'
                },
            )
        self.assertEqual(res.status_code, 200)

    def test_add_movie(self):
        res = self.client().post(
            '/movies',
            headers={
                'Authorization': EXECUTIVE_PRODUCER_JWT,
                },  
            json={
                'title': 'A New Movie',
                'release_year': 2023,
                },
            )
        self.assertEqual(res.status_code, 200)

    def test_add_movie_role_error(self):
        res = self.client().post(
            '/movies', 
            headers={
                'Authorization': CASTING_DIRECTOR_JWT,
                },
            json={
                'title':'A New Movie',
                'release_year':2023,
                },
            )
        self.assertEqual(res.status_code, 403)

    def test_unauthenticated_error(self):
        res = self.client().post(
            '/actors', 
            json={
                'age': 43,
                'name': 'Chris Pratt',
                'gender': 'Male'
                }
            )
        self.assertEqual(res.status_code, 401)

    def test_patch_actor(self):
        res = self.client().patch(
            '/actors/1',
            headers={
                'Authorization': EXECUTIVE_PRODUCER_JWT,
                }, 
            json={
                'name': 'Test Name',
                }
            )
        self.assertEqual(res.status_code, 200)

    def test_patch_actor_bad_request(self):
        res = self.client().patch(
            '/actors/0',
            headers={
                'Authorization': EXECUTIVE_PRODUCER_JWT,
                }, 
            json={
                'name': 'Test Name',
                }
            )
        self.assertEqual(res.status_code, 400)

    def test_patch_movie_bad_request(self):
        res = self.client().patch(
            '/movies/0',
            headers={
                'Authorization': EXECUTIVE_PRODUCER_JWT,
                }, 
            json={
                'title': 'Test Title'
                }
            )
        self.assertEqual(res.status_code, 400)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()