from mongoengine import connect, Document, ListField, StringField, IntField, DateTimeField, URLField, SequenceField, FloatField
import datetime

now = datetime.datetime.now()
now_no_seconds = now.isoformat(" ", "seconds")



class ProjectPosts(Document):
    title = StringField(required=True, max_length=120)
    description = StringField(required=True, max_length=5000)
    project_link = StringField(required=False, max_length=200)
    project_link_name = StringField(required=False, max_length=200)
    date_posted = DateTimeField(required=True, default=now_no_seconds)
    # image = ImageField(required=False)
    tags = ListField(StringField(max_length=50))
    slug = StringField(required=True, max_length=120)
    meta = {'collection': 'ProjectPosts'}


class ExperiencePosts(Document):
    title = StringField(required=True, max_length=120)
    position = StringField(required=True, max_length=120)
    description = StringField(required=True, max_length=5000)
    date_working = StringField(required=True, max_length=100)
    website_link = StringField(required=False, max_length=200)
    quote = StringField(required=False, max_length=500)
    date_posted = DateTimeField(required=True, default=now_no_seconds)
    # image = ImageField(required=False)
    tags = ListField(StringField(required=False, max_length=50))
    slug = StringField(required=True, max_length=120)
    meta = {'collection': 'ExperiencePosts'}


class EducationPosts(Document):
    title = StringField(required=True, max_length=120)
    degree = StringField(required=True, max_length=120)
    study_place = StringField(required=True, max_length=200)
    description = StringField(required=True, max_length=5000)
    quote = StringField(required=False, max_length=500)
    date_graduated = StringField(required=True, max_length=100)
    date_posted = DateTimeField(required=True, default=now_no_seconds)
    # image = ImageField(required=False)
    tags = ListField(StringField(max_length=50))
    slug = StringField(required=True, max_length=120)
    meta = {'collection': 'EducationPosts'}


class BlogPosts(Document):
    title = StringField(required=True, max_length=120)
    content = StringField(required=True, max_length=5000)
    author = StringField(required=True, max_length=120)
    date_posted = DateTimeField(required=True, default=now_no_seconds)
    # image = ImageField(required=False)
    tags = ListField(StringField(max_length=50))
    likes = IntField(default=0)
    dislikes = IntField(default=0)
    comments = ListField(StringField(max_length=500))
    slug = StringField(required=True, max_length=120)
    meta = {'collection': 'BlogPosts'}
