from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github
from datetime import datetime

load_dotenv(join(dirname(__file__), '.env'))

GITHUB_TOKEN = environ.get('GITHUB_TOKEN')

g = Github(login_or_token=GITHUB_TOKEN)
u = g.get_user()

for i in u.get_issues():
    print(i.title, datetime.now() - i.created_at)
