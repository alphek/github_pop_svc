import requests
from github_pop_svc.constants import GITHUB_API_URL
from django.conf import settings

# TODO making this a class and creating as a instance more proper
gh_session = requests.Session()
gh_settings = getattr(settings, "GITHUB", None)
if gh_settings:
    gh_session.auth = (gh_settings["username"], gh_settings["token"])


def get_repository_info(username, repository_name):
    response = gh_session.get(GITHUB_API_URL.format(username, repository_name))
    return response.json()


def is_repo_popular(num_stars, num_forks):
    return num_stars + 2 * num_forks >= 500

