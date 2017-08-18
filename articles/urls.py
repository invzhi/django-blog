from django.conf.urls import url

from .views import ArticleListView, ArticleDetailView, TaggedArticleListView, SearchView

app_name = 'articles'
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'^tagged/(?P<tags_with_plus>[\w\+-]+)/$', TaggedArticleListView.as_view(), name='tagged-list'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
]
