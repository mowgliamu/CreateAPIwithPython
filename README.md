# Create API with Python

A simple RESTful API for books database written in Flask framework using SQLAlchemy (ORM) and Marshmallow (Serialization/Deserialization).

## Pull Docker image from Google cloud
`docker pull gcr.io/bookapi-297922/bookapiimage:latest`

You can check that the image has been created successfully by running:

`docker images`

## Start the API by running the server in background
`docker run -it -d -p 8080:8080 docker.io/library/bookapi`

With `docker ps -a` you can check the container id and the port address on which the app is running. 

## Test Run
`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address (default is for GC app engine) running and CSVDATA is csvfile containing test data. A `mock.csv` is provided for test run.
An output file named `summary.txt` will be created describing the results, in addition there will also be a `tmp.log`.

## Tests with Postman
Individual tests can also be performed with Postman (highly recommended). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors (or other errors). 

