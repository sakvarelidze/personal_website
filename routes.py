from saba import *
from forms import *
from passlib.hash import sha256_crypt
from secrets import token_hex
from functools import wraps


# Custom Wraps


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You have to log in to see this page", "danger")
            return redirect(url_for('login'))
    return wrap


# Routes


@app.route('/', methods=['GET', 'POST'])
def index():

    # connect(db=MONGODB_NAME, host=MONGODB_HOST, username=MONGODB_USER, password=MONGODB_PASSWORD, port=27017)
    connect(db=MONGODB_NAME, host=MONGODB_HOST, port=27017)
    projects = ProjectPosts.objects()
    jobs = ExperiencePosts.objects()
    edus = EducationPosts.objects()
    
    return render_template('index.html', projects=projects, jobs=jobs, edus=edus)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    connect(db=MONGODB_NAME, host=MONGODB_HOST, port=27017)
    form = RegisterForm(request.form)

    # Check if user exists in mongodb database if not register
    if request.method == 'POST':
        # Get form fields
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm.data

        # Check if user already exists
        user = User.objects(username=username).first()
        if user:
            flash('Username already exists', 'danger')
            return redirect(url_for('signup'))

        # Check if email already exists
        user = User.objects(email=email).first()
        if user:
            flash('Email already exists', 'danger')
            return redirect(url_for('signup'))

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('signup'))

        # Hash password
        hashed_password = sha256_crypt.encrypt(str(password))

        # Create user object
        uid = token_hex(16)
        user = User(uid=uid, username=username, email=email, password=hashed_password)
        user.save()

        # Log user in
        session['logged_in'] = True
        session['username'] = username

        # Redirect to home page
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    connect(db=MONGODB_NAME, host=MONGODB_HOST, port=27017)
    form = LoginForm(request.form)
    # Log user in
    if request.method == 'POST':
        # Get form fields
        username = form.username.data
        password_candidate = form.password.data

        # Check if user exists in mongodb database
        user = User.objects(username=username).first()
        if user:
            # Check if password is correct
            password = user.password
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                # Redirect to home page
                return redirect(url_for('index'))
            else:
                flash('Invalid password', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Username not found', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html', form=form)


@app.route("/profile/logout/")
@is_logged_in
def logout():
    session.clear()
    flash("You have logged out", "success")
    return redirect(url_for('login'))