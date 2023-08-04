# myApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Use an empty path to match the root URL
     path('search/', views.search_jobs, name='search_jobs'),
]
