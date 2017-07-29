from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404

from .models import Article, Tag


class ArticleListView(ListView):
    model = Article
    ordering = ['-first_commit']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagArticleListView(ListView):
    template_name = 'article/tag_article_list.html'
    paginate_by = 10

    def __init__(self):
        self.tags = []

    def get_queryset(self):
        articles = Article.objects
        tags_name = self.args[0].split('+')
        for tag_name in tags_name:
            tag = get_object_or_404(Tag, name=tag_name)
            self.tags.append(tag)
            articles = articles.filter(tags=tag)
        return articles.order_by('-first_commit')

    def get_context_data(self, **kwargs):
        context = super(TagArticleListView, self).get_context_data(**kwargs)
        context['current_tags'] = self.tags
        context['tags'] = Tag.objects.all()
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


class AboutView(TemplateView):
    template_name = 'article/about.html'
