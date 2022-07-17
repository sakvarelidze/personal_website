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
