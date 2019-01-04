# This application runs a Flask web server and provides two urls.

This applications assumes that Redis queues are already install with default Config

Before we describe the urls lets start Flask and rq workers

## Starting Flask:
FLASK_APP=hello.py flask run

## Starting rq worker:
rq worker

Before running above commands make sure that your virtualenv is activated (if any) and the current working directory is the root of this repository

The url for making new request is *serveraddress*:*port*/give_wc/*url*
To view all resulst till now use *serveraddress*:*port*/

If everything is used as default then *serveraddress* will be localhost and *port* will be 5000