from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session

# .ENV import and MongoDB connection
from config import *
from mongo_models import *

# Initialize Flask App
app = Flask(__name__)
POSTS_IMAGES = os.path.join('static', 'post_images')


# Initialize config
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = POSTS_IMAGES
app.config['MONGODB_NAME'] = MONGODB_NAME
app.config['MONGODB_HOST'] = MONGODB_HOST
app.config['MONGODB_PORT'] = MONGODB_PORT
app.config['MONGODB_USER'] = MONGODB_USER

# Routes & Error Handlers
from routes import *
from error_handler import *


if __name__ == '__main__':
    app.secret_key = FLASK_SECRET_KEY
    app.run(debug=FLASK_APP_DEBUG, host=FLASK_APP_HOST, port=FLASK_APP_PORT)