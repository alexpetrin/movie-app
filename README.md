SUMMARY

    A casting agency app that allows users to view actors and movies. There are role-based permissions for casting directors and executive producers.


HOSTING

    This app is hosted on Heroku at the following URL.

    Heroku URL
    https://movie-app-now.herokuapp.com


AUTHENTICATION

    Roles are as follows:
    Unauthenticated - GET /actors and /movies
    Casting Director - GET and PATCH /actors and /movies, POST and DELETE /actors
    Executive Producer - GET, PATCH, POST, and DELETE /actors and /movies

    Postman has been set up for easy testing of these three roles. See the json file:
    postman_test.json

    Login screen can be found at:
    https://dev-82i1k4rjpl4gvtuf.us.auth0.com/authorize?audience=movie&response_type=token&client_id=WQoVaaRmIfA5zEA5Ocx4QL3XfOLfnUl0&redirect_uri=https://movie-app-now.herokuapp.com

    The following two users have been created for testing purposes:

    Email: alexpetrin2@gmail.com
    Password: Passw0rd
    Role: Executive Producer
    Sample JWT: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllNelVsOHVvZXVQclFTTV9oWXJTSiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmkxazRyanBsNGd2dHVmLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkxNWMxMTY1YTFhODJlZjUwZDAyM2IiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTY3MDQ3MDg2MiwiZXhwIjoxNjcwNTU3MjYyLCJhenAiOiJXUW9WYWFSbUlmQTV6RUE1T2N4NFFMM1hmT0xmblVsMCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.P1Nf6Yg43BGFKwwWVB_Mlnew9IDPrRK63-UekMMJEqsCMsZpnkdPnWGD86YYhRN2mMmaD6bYqfRs-WlnkgHqFkUD-5Hjluu3cvPGOYxTgVXNKftAibkVNMSy4-OtAHbzW9LSaTQvLPGtz-Qu1eP53numMIs9BaAgXBmbNoy5oNQYrjOdzWrTcC6mJg5qFxSZTxcYKatMHz5thIuGV4nX8of51b1hDezepYI27ZC57V7RRbtWOiKoG_Id74chcGwO5GjuAtN9Co1xelyR0d02QLFK4B0ZAQ_ToPLUiL46IkHyF-1IzVxkDQOdx3wsKVXolEnOWyq6WauGUpRw84WEuA

    Email: joshua1vnine@gmail.com
    Password: Passw0rd
    Role: Casting Director
    Sample JWT: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IllNelVsOHVvZXVQclFTTV9oWXJTSiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MmkxazRyanBsNGd2dHVmLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzVjMjcyYTcyNDMyNzZkZTQ3ODZjZjYiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTY3MDQ3MDIwMCwiZXhwIjoxNjcwNTU2NjAwLCJhenAiOiJXUW9WYWFSbUlmQTV6RUE1T2N4NFFMM1hmT0xmblVsMCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.RMhuP23910Iy9OMlKcd6GCSNsk_tRWk4K5n31GWP9qBZxqNDxY6VjRZaTyJSRcy2DQEGuRUi1HX7sE_Dj9QuiZY6yAzAAhyAI8E5gohDgza9PCK45oSXpqUZFtJfoz0tyG_CpJNSemDP7ebh_OWMVgPVWfvW1hJa5IseUnOYkbD1r-ScbXbO61EMuOIvOdoIZSFy7LYm5aEEhErTvI5VZCA8tdBB9Q0OSoZjZ2uaNZNseyYSOxcwuoWREXmvnD2Zfhu1pbkKfzvgf-ve9S-KMatJJ8zL_RCzgnVMBjVFFgBto3tKSfbOhsRD9_CyGUjj4IhrvhlaVBt3TEwIY876aQ


TESTING

    Run test_app.py
    The above JWTs are included for role and authentication testing.
