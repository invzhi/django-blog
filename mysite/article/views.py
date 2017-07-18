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

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.args[0])
        return Article.objects.filter(tags=self.tag).order_by('-first_commit')

    def get_context_data(self, **kwargs):
        context = super(TagArticleListView, self).get_context_data(**kwargs)
        context['current_tag'] = self.tag
        context['tags'] = Tag.objects.all()
        context['article_count'] = Article.objects.count()
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        object = super(ArticleDetailView, self).get_object()
        object.views += 1
        object.save()
        return object


# def search(request):
#     q = request.GET.get('q')
#     # TODO
#     context = {}
#     return render(request, 'article/articles.html', context)


class SearchView(ListView):
    model = Article


class AboutView(TemplateView):
    template_name = 'article/about.html'
