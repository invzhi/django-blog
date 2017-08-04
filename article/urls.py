from django.conf.urls import url

from .views import ArticleListView
from .views import ArticleDetailView
from .views import TaggedArticleListView
from .views import SearchView

app_name = 'article'
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^tagged/([\w\+-]+)/$', TaggedArticleListView.as_view(), name='tagged-article-list'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
]
