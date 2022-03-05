from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.cache import cache
from github_pop_svc.github_util import get_repository_info, is_repo_popular
from github_pop_svc.constants import GITHUB_REPO_INFO_CACHE_INTERVAL


class GithubPopViewSet(viewsets.ViewSet):
    # Used cache in front of Github api request to lower average response time and prevent possible DDOS attack
    # Also can be added api limit or some more preventions to make it safer
    def retrieve_github_popularity(self, request, username, repository_name):
        cache_key = "{}_{}_is_popular".format(username, repository_name)
        is_popular = cache.get(cache_key)
        print(is_popular)
        if is_popular is None:
            info_json = get_repository_info(username, repository_name)
            is_popular = is_repo_popular(info_json["stargazers_count"], info_json["forks_count"])
            # current cache expire time 1 hour, can be changed from constant file
            # if change in this will be more frequent can be given by some external tool as well
            cache.set(cache_key, is_popular, GITHUB_REPO_INFO_CACHE_INTERVAL)
        return Response({"status": "success", "data": {"is_popular": is_popular}}, status=status.HTTP_200_OK)
