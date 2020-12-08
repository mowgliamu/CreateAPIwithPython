# Create API with Python
A simple RESTful API for books database in Flask using SQLAlchemy and Marshmallow.

## Run API using Google Cloud App Engine
Click below to start the server:

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://bookapi-297922.uc.r.appspot.com/books)


## Test Run
`python3 create_post_request.py [URL] [CSVDATA]`

Where URL is the server address (default is for GC app engine) running and CSVDATA is csvfile containing test data. A `mock.csv` is provided for test run.
An output file named `summary.txt` will be created describing the results, in addition there will also be a `tmp.log`.

## Test with Postman
Individual tests can also be performed with Postman (recommended) using either the GC server or locally (see below). Examples from `mock.csv` are provided in `postman_examples.txt`. These examples will demonstrate the functionality of the API including failure scenarios based on schema validation errors.

## Running locally using docker image
If for some reason you would like to set up the server on your local machine, clone the repo on your local machine and dockerize using the command given below. You can also pull the pre-built image from Google cloud. Once the image is created, you can run it using the docker run command given below. This will start the API server on localost:5000. You can then perform the example run as mentioned above, or have fun with Postman!

### Docker Build Image
`docker build -t bookapi .` 

### Docker Run
`docker run -it -d -p 5000:5000 docker.io/library/bookapi`

### Pull image from Google cloud
`docker pull gcr.io/bookapi-297922/bookapiimage:latest`
