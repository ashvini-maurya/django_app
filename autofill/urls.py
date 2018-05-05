from django.conf.urls import patterns, url
from autofill import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'))