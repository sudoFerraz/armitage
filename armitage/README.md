Flask Assesment
===========

**version 0.0.0.0.0.1 :)**

This is a python assessment from Klarna. Done by Gabriel Ferraz sudoferraz@gmail.com.
The solution was built using a flask application that exposes a get and post endpoint for each of the provided math calculations. You can choose the dockerized or virtual environment approach to run it locally. Be aware that due to python limitations, some functions as the ackermann, when given big inputs can throw your request off. 
As it was not in the scope of this task and I literally didn't had the time to implement as this week was crazy, these problems were not addressed. Altought not done, proposed solutions for this would be spinning up different threads, on non recursive implementations of it, storing the value on a table that the user could then read later. (There is a POC on fibonacciService and fibonacciController) PS. I literally submitted this on the last day on the last hour, if you would like to see me implementing these approaches, please get back to me with few more days and I can do it, as I only really worked on this project today after 18:00 :)

If this would be a large scale application, instead of using different threads, the suggested approach would be using message queues with a framework to handle the jobs like Celery, in this way you could have multiple containers orchastrated in a way that only one would consume the message and execute the job.

The easiest approach is to use docker btw ->

```shell
# if virtualenv is not installed
sudo pip install virtualenv # or pip install --user virtualenv

```

Getting Started
===============

You're advised to use venv from here on. In your project folder,
create and enable it like this, or use the one provided:

Creating a new one:
```shell
python3 -m venv venv
. venv/bin/activate  # [.csh|.fish]

# install required packages
pip install -r requirements.txt

# loads env variables and runs the project in development mode
export FLASK_APP=flaskMathApp
export FLASK_ENV=development
source /venv/bin/activate && flask run
```

Using the one provided:

```shell
#if you are using another shell other then bash
bash

source /venv/bin/activate

```

Getting Started With Docker
===========================

Given you have up-to-date docker installed in your machine,
all you need to do is:

```shell
# build container image and runs it
docker-compose up --build

# or run it on the background
docker-compose up -d --build
```

Environment Variables
=====================

Be aware that you might need to tweak the environment variables for production
mode. They are available at `Dockerfile` and at the activation script from the venv. If using Docker,
you can even provide them inline.

==============================

Usage of the app
============

As it is known, ackermann function and factorial are functions that grow rapdily in size, and they need to be ran in the background. Because of this, if you experience normal behavior with smaller inputs on the endpoints, but get a bad request with larger inputs, you should be using the threaded versions of each (That I didn't finished implementing :D )

You can query endpoints with a GET and a POST request on each

```shell
# Finding the N-th number on the fibonacci sequence
GET localhost:5000/fibonacci/<fibonacciStep>

POST localhost:5000/fibonacci Json body: {'fibonacciStep': 0 }

# Finding the factorial of a non negative integer number
GET localhost:5000/factorial/<factorialTarget>

POST localhost:5000/factorial Json body: {'factorialTarget': 12}

#Finding the ackermann function result for variables M and N
GET localhost:5000/ackermann/ackermann/1/1

POST locashot:5000/ackermann Json body: {'m': 1, 'n': 1}

```

### You can monitor and profile each endpoint and it's functions accessing:

localhost:5000/dashboard with the credentials admin/admin

Clicking on an endpoint on the dashboard, and then clicking on "Profile", you can see each request individually and the time each took to complete


Other topics
============

## Blueprints

You can create blueprints easily with `flask new-app <name>`. The will live, by default
at `apps` folder.

# Extensions

## FLask-MonitoringDashboard

Monitoring dashboard provides a graphical interface out of the box to monitor enpoints and profile them regarding number of requests, time taken and general usage.

## Docker

Docker was chosen for this assesment as it would easily recriate the environment between different machines for testing purposes

## Pytest

Pytest makes it easy to run and compare all the tests that were made on a single commnad, finding all different test components and agreggating them into a single suite

## SqlAlchemy

Used in the POC to create the threaded versions of each endpoint

```shell
# runs test suite
python3 -m pytest -v
```

