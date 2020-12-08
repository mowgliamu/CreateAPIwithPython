# Create API with Python
A simple RESTful API for books database in Flask using SQLAlchemy and Marshmallow.

## Pull Docker image from Google cloud
`docker pull gcr.io/bookapi-297922/bookapiimage:latest`

Check that you have the image by doing
`docker images`

## Start the API by running the server in background
`docker run -it -d -p 8080:8080 docker.io/library/bookapi`

By doing `docker ps -a` you can check the status of the app. It will also provide you the container id and the port address on which the app is running. 

## Test Run
`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address (default is for GC app engine) running and CSVDATA is csvfile containing test data. A `mock.csv` is provided for test run.
An output file named `summary.txt` will be created describing the results, in addition there will also be a `tmp.log`.

## Test with Postman
Individual tests can also be performed with Postman (recommended) using either the GC server or locally (see below). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors.

