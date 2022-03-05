from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('github_pop/', include('github_pop_svc.urls')),
    # More health check options can be added or can be completely customized
    # https://django-health-check.readthedocs.io/en/latest/
    path('health_check/', include('health_check.urls')),
    path('docs/', include('github_pop_svc.doc_urls'))
]