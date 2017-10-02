"""URL Definition for JoshGrid application."""
from django.conf.urls import url

from bucketlist_app import views

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^logout/$', views.logout_view, name="auth_logout")
]
