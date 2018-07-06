from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gmailAuthenticate', views.gmail_authenticate, name='gmail_authenticate'),
    url(r'^oauth2callback', views.auth_return),
    url(r'^$', views.home, name='home'),
]
