# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Twitter API
API_KEY = os.environ.get("API_KEY")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
CALLBACK_URL = os.environ.get("CALLBACK_URL")
HONDA_ACCESS_TOKEN = os.environ.get("HONDA_ACCESS_TOKEN")
HONDA_ACCESS_TOKEN_SECRET = os.environ.get("HONDA_ACCESS_TOKEN_SECRET")

# MySQL
MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")