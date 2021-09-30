# Bookstore-ML

This repository includes the backend as well as ML logic for our bookstore.
We will also use it as the common backend across all the methods of Frontend we are implementing.

## Environment setup

We assume that Python3, pip and venv are already installed on your device.

```sh
# clone repository locally
$ git clone https://github.com/AOSP-NIT-Surat/Bookstore-ML.git
# open the directory
$ cd Bookstore-ML
# create venv environment
$ python3 -m venv env
$ pip3 install -r requirements.txt
# export dev environment
$ export FLASK_ENV=development
# start the flask server
$ flask run
```

## Tech Stack

- Flask
- OpenCV
- Tensorflow
- Postgres
- Elastic Search
