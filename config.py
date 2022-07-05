from dotenv import load_dotenv
import os

load_dotenv()

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
FLASK_APP_DEBUG = os.getenv("FLASK_APP_DEBUG")
FLASK_APP_HOST = os.getenv("FLASK_APP_HOST")
FLASK_APP_PORT = os.getenv("FLASK_APP_PORT")

MONGODB_NAME = os.getenv("MONGODB_NAME")
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_PORT = os.getenv("MONGODB_PORT")
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")