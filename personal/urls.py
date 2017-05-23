from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^projects.html$', views.projects, name='projects'),
    url(r'^contact/$', views.contact, name='contact'),
]
