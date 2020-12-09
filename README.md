# Create API with Python

RESTful API for books database written in Flask framework using SQLAlchemy (ORM) and Marshmallow (Serialization/Deserialization).

## Pull Docker image from Google cloud
`docker pull gcr.io/bookapi-297922/bookapiimage:latest`

You can check that the image has been created successfully by running:

`docker images`

## Start the API by running the server in background
`docker run -it -d -p 8080:8080 docker.io/library/bookapi`

With `docker ps -a` you can check the container id and the port address on which the app is running. 

## Test Run
A tiny book database has been provided in `mock.csv`. To post the entries in the database using the API, run the following:

`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address (http://0.0.0.0:8080) and CSVDATA is csvfile containing test data (`mock.csv` if not provided). An output file named `summary.txt` will be created describing the results, indicating the successful and failed entries. If you have a sqlite3 database file, it can be converted to csv format by a utility script provided in [https://github.com/mowgliamu/convert-db-to-csv]  

## Tests with Postman
Individual tests can also be performed with Postman (highly recommended). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors (or other errors). 

## Development Run
If you would like to run the API in development mode on your local machine, it can be done as follows:

- Clone the repo
- Change port from 8080 to 5000 in `app.py`
- Install dependencies: `pip3 install -r requirements.txt`
- Start the server: `flask run`
- Run the test: `python3 create_post_request.py [URL] [CSVDATA]`
- Or play with Postman!

In the development mode, you can explicitly see how the sqlite database file `catalogue.db` is getting update after each HTTP request. 
