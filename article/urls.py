from django.conf.urls import url

from .views import ArticleListView
from .views import ArticleDetailView
from .views import TaggedArticleListView
from .views import SearchView
from .views import AboutView

app_name = 'article'
urlpatterns = [
    url(r'^$', ArticleListView.as_view()),  # TODO: beautiful index
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),
    url(r'^articles/tagged/([\w-]+)/$', TaggedArticleListView.as_view(), name='tag-article-list'),
    url(r'^articles/tagged/([\w\+-]+)/$', TaggedArticleListView.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]
