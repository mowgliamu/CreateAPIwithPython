# Create API with Python

RESTful API for books database written in Flask framework using SQLAlchemy (ORM) and Marshmallow (Serialization/Deserialization).

## API Server 
The API is up-and-running at [https://bookapi-297922.uc.r.appspot.com/books], which has been created using Google Cloud App Engine. All the source and configuration files are located in `src/`.

## Running the test with mock data
Clone/download the `example`. A small book database has been provided in `mock.csv`. To post the entries in the database using the API, run the following:

`pip3 install -r requirements.txt`

`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address [default https://bookapi-297922.uc.r.appspot.com/books] and CSVDATA is csvfile containing test data (default `mock.csv`). An output file named `summary.txt` will be created describing the results, indicating the successful and failed entries.

## Tests with Postman
Individual tests can also be performed with Postman (highly recommended). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors.

## Development Run (on local machines)
If you would like to run the API in development mode on your local machine, it can be done as follows:

- Clone/download the repo
- In the `src/` directory:
	- Install dependencies: `pip3 install -r requirements.txt`
	- Create a file named `.flaskenv` and add `FLASK_ENV=development`
	- Start the server: `flask run`
- In `example`, run the test: `python3 create_post_request.py [URL] [CSVDATA]` (Change URL to your local port address now)
- Or play with Postman!

In the development mode, you can explicitly see how the sqlite database file `catalogue.db` is getting updated after each HTTP request. 

## Docker pull
If for some reason you would like to work with the docker image, you can pull it using:

`docker pull gcr.io/bookapi-297922/bookapiimage:latest`
