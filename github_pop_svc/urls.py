from django.urls import path
from github_pop_svc.views import GithubPopViewSet

urlpatterns = [
    path('repos/<str:username>/<str:repository_name>/', GithubPopViewSet.as_view({
        'get': 'retrieve_github_popularity'
    }), name="retrieve_github_popularity")
]
