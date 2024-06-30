from django.urls import path, include
from . import views



urlpatterns = [
    path('api/', views.home, name="newuser"),
    path('accounts/', include('allauth.urls')),
]
