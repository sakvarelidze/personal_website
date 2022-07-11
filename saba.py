from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import secrets

# Custom import
from config import *
from mongo_models import *

# Initialize Flask App
app = Flask(__name__)
POSTS_IMAGES = os.path.join('static', 'post_images')


# Initialize additional config
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = POSTS_IMAGES
app.config['MONGODB_NAME'] = MONGODB_NAME
app.config['MONGODB_HOST'] = MONGODB_HOST
app.config['MONGODB_PORT'] = MONGODB_PORT
app.config['MONGODB_USER'] = MONGODB_USER

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():

    #connect(db=MONGODB_NAME, host=MONGODB_HOST, username=MONGODB_USER, password=MONGODB_PASSWORD, port=27017)
    connect(db=MONGODB_NAME, host=MONGODB_HOST, port=27017)
    projects = ProjectPosts.objects()
    jobs = ExperiencePosts.objects()
    edus = EducationPosts.objects()
    
    return render_template('index.html', projects=projects, jobs=jobs, edus=edus)


@app.route('/admin', methods=['GET', 'POST'])
def index_admin():

    return "TBA"

@app.route('/blog', methods=['GET','POST'])
def blogs():

    return "<h1 align='center'> Blog Page is under construction </h1>"


# Error handler
from error_handler import *


if __name__ == '__main__':
    app.secret_key = FLASK_SECRET_KEY
    app.run(debug=FLASK_APP_DEBUG, host=FLASK_APP_HOST, port=FLASK_APP_PORT)