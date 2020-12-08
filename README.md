# Create API with Python
A simple RESTful API for books database in Flask using SQLAlchemy and Marshmallow.

## Pull Docker image from Google cloud
`docker pull gcr.io/bookapi-297922/bookapiimage:latest`

## Start the API by running the server in background
`docker run -it -d -p 5000:5000 docker.io/library/bookapi`

## Test Run
`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address (default is for GC app engine) running and CSVDATA is csvfile containing test data. A `mock.csv` is provided for test run.
An output file named `summary.txt` will be created describing the results, in addition there will also be a `tmp.log`.

## Test with Postman
Individual tests can also be performed with Postman (recommended) using either the GC server or locally (see below). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors.

