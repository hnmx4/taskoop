from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github
from datetime import datetime
from rtmbot.core import Plugin


class ReplyTask(Plugin):
    def process_message(self, data):
        load_dotenv(join(dirname(__file__), '.env'))

        g = Github(login_or_token=environ.get('GITHUB_TOKEN'))
        u = g.get_user()

        res = ''
        for i in u.get_issues():
            msg = i.title + ':' + str(datetime.now() - i.created_at)
            res += msg + '\n'

        if 'task' in data['text']:
            self.outputs.append([environ.get('CHANNEL_ID'), res])
