import settings
from github import Github

g = Github(login_or_token=settings.GITHUB_TOKEN)
u = g.get_user()

print(u.get_issues())  # u.get_issues().get_page() ???
