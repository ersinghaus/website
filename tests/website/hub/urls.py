from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^$', views.about),
    url(r'^$', views.math),
    url(r'^$', views.science),
    url(r'^$', views.history),
    url(r'^$', views.art),
    url(r'^$', views.signup),
    url(r'^$', views.register),
]
