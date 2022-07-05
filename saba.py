from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import secrets

# Custom import
from config import *
from mongo_models import *

# Initialize Flask App
app = Flask(__name__)
POSTS_IMAGES = os.path.join('static', 'post_images')


# Initialize additional config
app.secret_key = FLASK_SECRET_KEY
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DB
app.config['MYSQL_CURSORCLASS'] = MYSQL_CURSORCLASS
app.config['UPLOAD_FOLDER'] = POSTS_IMAGES
app.config['MONGODB_NAME'] = MONGODB_NAME
app.config['MONGODB_HOST'] = MONGODB_HOST
app.config['MONGODB_PORT'] = MONGODB_PORT
app.config['MONGODB_USER'] = MONGODB_USER
app.config['RECAPTCHA_PUBLIC_KEY'] = RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = RECAPTCHA_PRIVATE_KEY

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():

    connect(db=MONGODB_NAME, host=MONGODB_HOST, username=MONGODB_USER, password=MONGODB_PASSWORD, port=27017)
    projects = ProjectPosts.objects()
    jobs = ExperiencePosts.objects()
    edus = EducationPosts.objects()
    
    return render_template('index.html', projects=projects, jobs=jobs, edus=edus)


@app.route('/admin', methods=['GET', 'POST'])
def index_admin():

    return "<h1 align='center'> Admin page is under construction </h1>"

@app.route('/blog', methods=['GET','POST'])
def blogs():
    return "<h1 align='center'> Blog Page is under construction </h1>"

# Error handler
from error_handler import *


if __name__ == '__main__':
    app.secret_key = FLASK_SECRET_KEY
    app.run(debug=FLASK_APP_DEBUG, host=FLASK_APP_HOST, port=FLASK_APP_PORT)