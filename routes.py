from saba import *

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():

    #connect(db=MONGODB_NAME, host=MONGODB_HOST, username=MONGODB_USER, password=MONGODB_PASSWORD, port=27017)
    connect(db=MONGODB_NAME, host=MONGODB_HOST, port=27017)
    projects = ProjectPosts.objects()
    jobs = ExperiencePosts.objects()
    edus = EducationPosts.objects()
    

    return render_template('index.html', projects=projects, jobs=jobs, edus=edus)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if username and password and email:
            if User.objects(username=username).first():
                flash('Username already exists')
                return redirect(url_for('signup'))
            else:
                user = User(username=username, password=password, email=email)
                user.save()
                flash('User created successfully')
                return redirect(url_for('login'))
        else:
            flash('Please fill all the fields')
            return redirect(url_for('signup'))
    return render_template('signup.html')


@app.route('/admin', methods=['GET', 'POST'])
def index_admin():

    return "TBA"

@app.route('/blog', methods=['GET','POST'])
def blogs():

    return "<h1 align='center'> Blog Page is under construction </h1>"