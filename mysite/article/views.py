from django.http import QueryDict
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Tag

per_page = 5
# per_page = 10
tags = Tag.objects.all()


def index(request):
    # archive
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    # tag
    tag_name = request.GET.get('tag')
    # page
    page = request.GET.get('page') or 1

    if tag_name is None:
        articles = Article.objects.all()
    else:
        tag = get_object_or_404(Tag, name=tag_name)
        articles = tag.article_set.all()

    date = {}
    if year is not None:
        date.update({'first_commit__year': year})
    if month is not None:
        date.update({'first_commit__month': month})
    if day is not None:
        date.update({'first_commit__day': day})

    if date:
        articles = articles.filter(**date)

    articles = articles.order_by('-first_commit')

    paginator = Paginator(articles, per_page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    q = request.GET.urlencode()
    q = QueryDict(q, mutable=True)
    try:
        q.pop('page')
    except KeyError:
        pass
    finally:
        parameters = q.urlencode()
        if parameters:
            parameters += '&'

    context = {
        'articles': articles,
        'tags': tags,
        'parameters': parameters,
    }
    return render(request, 'article/articles.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    updated_views = article.views + 1
    Article.objects.filter(pk=article_id).update(views=updated_views)
    context = {
        'article': article,
        'tags': tags,
    }
    return render(request, 'article/detail.html', context)


def search(request):
    q = request.GET.get('q')
    # TODO
    context = {}
    return render(request, 'article/articles.html', context)


def about(request):
    context = {
        # 'article': article,
        # 'tags': tags,
    }
    return render(request, 'article/about.html', context)
