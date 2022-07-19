from dotenv import load_dotenv
import os

load_dotenv()

# Flask App Config
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
FLASK_APP_DEBUG = os.getenv("FLASK_APP_DEBUG")
FLASK_APP_HOST = os.getenv("FLASK_APP_HOST")
FLASK_APP_PORT = os.getenv("FLASK_APP_PORT")

# MongoDB config
MONGODB_NAME = os.getenv("MONGODB_NAME")
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_PORT = os.getenv("MONGODB_PORT")
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

# MySQL config
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")