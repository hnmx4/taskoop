from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

GITHUB_TOKEN = environ.get('GITHUB_TOKEN')
