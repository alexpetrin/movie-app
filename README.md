# Movie App Backend

## Summary

This projet is designed to demonstrate the backend of a simple movie listing portal, enabling users to create actor and movie profiles. The backend is designed to work for two types of users: casting directors and executive producers. Actor and movie profile information can be viewed but not edited by public users. 

Casting directors can view, post, update, and delete actors and view and update movies.
Executive producers can view, post, update, and delete both actors and movies.

Users must be authorized to be able to perform role-based requests to the backend via API described below. 

Authorization of users is enabled via Auth0 in which two seperate roles (casting directors and executive producers) have been created and assigned seperate permissions.

## Project dependencies

The project depends on the latest version of Python 3.x which we recommend to download and install from their official website and use a virtual environment to install all dependencies.

## PIP dependencies

After having successfully installed Python, navigate to the root folder of the project (the project must be forked to your local machine) and run the following in a command line:

```
pip3 install -r requirements.txt
```

This will install all the required packages to your virtual environment to work with the project.

## Database setup

The `models.py` file contains connection instructions to the Postgres database, which must also be setup and running. Provide a valid username and password, if applicable.

1. If the default `postgres` database does not exist already, create a database with name `postgres` using Psql CLI:

`createdb postgres`

2. Initiate and migrate the database with the following commands in command line:

```
python3 manage.py db init
python3 manage.py db migrate -m "Initial migration"
python3 manage.py db upgrade
```

This will create all necessary tables and relationships to work with the project.

## Data Modelling

The data model of the project is provided in `models.py` file in the root folder. The following schema for the database and helper methods are used for API behaviour:

- There are two tables created: Actor and Movie.
- The Actor table includes the fields name, age, and gender. Both the "Casting Director" role and "Executive Producer" role can create, update, or delete from this table. The information can be retrieved by any user.
- The Movie table includes the fields title and release_year. The "Executive Producer" role can create, update, or delete from this table. The "Casting Director" role can update but not create or delete. The information can be retrieved by any user.

## Running the local development server

All necessary credential to run the project are provided in the `setup.sh` file. The credentials can be enabled by running the following command:

```
source setup.sh
```

To run the API server on a local development environmental the following commands must be additionally executed:

### On Linux: export
```
export FLASK_APP=app.py
export FLASK_ENV=development
```

### On Windows: set
```
set FLASK_APP=app.py
set FLASK_ENV=development
```

### API Server

All accessable endpoints of the project are located in the `app.py` file.

Run the following command in the project root folder to start the local development server:

```
flask run
```

## RBAC credentials and roles

Auth0 was set up to manage role-based access control for two users. The API documentation below describes, among others, by which user the endpoints can be accessed. Access credentials and permissions are handled with JWT tockens which must be included in the request header. 

### Permissions

Users can access API endpoints that have the following permission requirements:

`'post:actor'` - Post actor information to the database
`'post:movie'` - Post movie information to the database
`'patch:actor'` - Edit actor information by id
`'patch:movie'` - Edit movie information by id
`'delete:actor'` - Delete actor by id from the database
`'delete:movie'` - Delete movie by id from the database

There are also publicly available endpoints that do not require authorization. This is done to ensure every user can see the general information about actors and movies.

## API endpoints

### Public endpoints

#### GET '/actors'
- Fetches a json list of actors from the database.
- Request Arguments: None
- Returns: A JSON object listing the actors in the database.

Sample curl request:
`curl -X GET https://movie-app-now.herokuapp.com/actors`

Sample response:
```
[{
    "age":99,
    "gender":"Male",
    "id":1,
    "name":"Chris Pratt"
}]
```
#### GET '/movies'
- Fetches a json list of movies from the database.
- Request Arguments: None
- Returns: A JSON object listing the movies in the database.

Sample curl request:
`curl -X GET https://movie-app-now.herokuapp.com/movies`

Sample response:
```
[{
    "id":3,
    "release_year":2013,
    "title":"Frozen"
}]
```

### Endpoints accessible by Casting Director
The Casting Director can access all of the above endpoints plus the endpoints in this section

#### POST '/actors/'
- Adds a new actor to the database.
- Request Arguments: A JSON formatted object with keys 'name', int 'age', 'gender'
- Returns: A success code on completion.

Sample curl request:
`curl -d '{"age":43,"gender":"Male","name":"Chris Pratt"}' -H "Content-Type: application/json" -H "Authorization: Bearer $CASTING_DIRECTOR_JWT" -X POST https://movie-app-now.herokuapp.com/actors`

Sample response:
```
[{
    "success": true
}]
```

#### DELETE '/actors/<int:actor_id>'
- Deletes actor by id from the database.
- Request Arguments: None
- Returns: A success code on completion.

Sample curl request:
`curl -H "Authorization: Bearer $CASTING_DIRECTOR_JWT" -X DELETE https://movie-app-now.herokuapp.com/actors/1`

Sample response:
```
[{
    "success": true
}]
```

#### PATCH '/actors/<int:actor_id>'
- Updates actor information by id.
- Request Arguments: A JSON formatted object with optional keys 'name', int 'age', 'gender'
- Returns: A success code on completion.

Sample curl request:
`curl -d '{"name": "Updated Name"}' -H "Content-Type: application/json" -H "Authorization: Bearer $CASTING_DIRECTOR_JWT" -X PATCH https://movie-app-now.herokuapp.com/actors/1`

Sample response:
```
[{
    "success": true
}]
```

#### PATCH '/movies/<int:movie_id>'
- Updates movie information by id.
- Request Arguments: A JSON formatted object with optional keys 'title', int 'release_year'
- Returns: A success code on completion.

Sample curl request:
`curl -d '{"title": "Updated Title"}' -H "Content-Type: application/json" -H "Authorization: Bearer $CASTING_DIRECTOR_JWT" -X PATCH https://movie-app-now.herokuapp.com/movies/1`

Sample response:
```
[{
    "success": true
}]
```

### Endpoints accessible by Executive Producer
The Executive Producer can access all of the above endpoints plus the endpoints in this section

#### POST '/movies/'
- Adds a new movie to the database.
- Request Arguments: A JSON formatted object with keys 'title', int 'release_year'
- Returns: A success code on completion.

Sample curl request:
`curl -d '{"title":"Frozen","release_year":2013}' -H "Content-Type: application/json" -H "Authorization: Bearer $CASTING_DIRECTOR_JWT" -X POST https://movie-app-now.herokuapp.com/movies`

Sample response:
```
[{
    "success": true
}]
```

#### DELETE '/movies/<int:movie_id>'
- Deletes movie by id from the database.
- Request Arguments: None
- Returns: A success code on completion.

Sample curl request:
`curl -H "Authorization: Bearer $EXECUTIVE_PRODUCER_JWT" -X DELETE https://movie-app-now.herokuapp.com/movies/1`

Sample response:
```
[{
    "success": true
}]
```

## Testing

The testing of all endpoints was implemented with unittest. Each endpoint can be tested with one success test case and one error test case. RBAC feature can also be tested for company user and candidate user.

All test cases are soted in `test_app.py` file in the project rool folder.

Before running the test application, run `source setup.sh`

Then create movieapp_test database using Psql CLI:
`createdb movieapp_test`

Using the command line interface run the test file:

`python3 test_app.py`

A Postman script has also been created for easy testing of these roles. See the json file:
`postman_test.json`


## Heroku Deployment and Base URL

The backend application has been deployed on Heroku and can be accessed live at
```
https://movie-app-now.herokuapp.com
```