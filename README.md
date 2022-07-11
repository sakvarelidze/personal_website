# Personal website built using Flask and Mongoengine

I've created this website as an "Online Portfolio Thingy". There's still lots of things missing which will be added over time.

## How to run

First and foremost install the requirements (if you are planning to run it without docker-compose)

```python3
python3 -m pip install -r requirements.txt
```

Serve it with gunicorn

```python3
gunicorn -b 0.0.0.0:5000 saba:app
```

## TODO

* ~~Implement MongoDB~~
* Add admin panel for content management.
* Add contact us logic
* Add blogposts page
* Add comments field for blogposts
* ~~Containerize the application~~
* ~~Write docker-compose script to run App, MongoDB and Mongo-express altogether~~

## How to use docker-compose

Firstly edit .env.example as necessary, afterwards run

```Docker
docker-compose up -d
```

This will create a network named "webservices" and pull 3 containers
