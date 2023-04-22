
from django.contrib import admin
from django.urls import include, path
from .root import api_root
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('surveys/', include('survey.urls')),
    path('root/', api_root ,name='root'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
