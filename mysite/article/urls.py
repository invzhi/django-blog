from django.conf.urls import url

from . import views

app_name = 'article'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^articles/$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/$', views.about, name='about'),
]
