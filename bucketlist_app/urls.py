"""URL Definition for JoshGrid application."""
from django.conf.urls import url

from bucketlist_app import views

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
]
