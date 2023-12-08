from django.urls import path
from .views import doc_home

urlpatterns = [
    path("home/", doc_home, name="home"),
]
