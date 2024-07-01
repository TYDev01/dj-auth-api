from django.urls import re_path as url, path
from .views import useLogin


urlpatterns = [
    path('log/', useLogin)
]
