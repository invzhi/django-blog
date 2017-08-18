from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from articles.models import Article, Tag


class ArticleListView(ListView):
    model = Article
    ordering = ['-first_commit']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.iterator()
        return context


class TaggedArticleListView(ListView):
    template_name = 'articles/tagged_article_list.html'
    paginate_by = 10

    def tags(self):
        tag_list = self.kwargs['tags_with_plus'].split('+')
        for tag_name in set(tag_list):
            tag = get_object_or_404(Tag, name=tag_name)
            yield tag

    def get_queryset(self):
        articles = Article.objects
        for tag in self.tags():
            articles = articles.filter(tags=tag)
        return articles.order_by('-first_commit')

    def get_context_data(self, **kwargs):
        context = super(TaggedArticleListView, self).get_context_data(**kwargs)
        context['current_tags'] = self.tags
        context['tags'] = Tag.objects.iterator()
        context['article_count'] = Article.objects.count()
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.views += 1
        obj.save()
        return obj


# def search(request):
#     q = request.GET.get('q')
#     # TODO
#     context = {}
#     return render(request, 'article/articles.html', context)


class SearchView(ListView):
    model = Article
