from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('github_pop/', include('github_pop_svc.urls'))
]