from random import randint

from django.shortcuts import reverse
from django.test import TestCase

from ..models import Article, Tag


class ViewTest(TestCase):
    def setUp(self):
        number_of_tags = 10
        number_of_articles = 50
        for tag_num in range(number_of_tags):
            Tag.objects.create(name='tag%s' % tag_num)
        self.tags = Tag.objects.all()
        for article_num in range(number_of_articles):
            article = Article.objects.create(title='Article %s' % article_num,
                                             content='Content %s\nThis is a article for django test.' % article_num)
            random_tags = []
            for tag in self.tags:
                if randint(0, 1):
                    random_tags.append(tag)
            article.tags.add(*random_tags)

    def test_article_list_view(self):
        resp = self.client.get(reverse('articles:article-list'))
        self.assertEqual(resp.status_code, 200)

    def test_tagged_article_list_view(self):
        for tag in self.tags:
            resp = self.client.get(reverse('articles:tagged-article-list', args=[tag]))
            self.assertEqual(resp.status_code, 200)

    def test_article_detail_view(self):
        for article in Article.objects.all():
            resp = self.client.get(reverse('articles:article-detail', args=[article.id]))
            self.assertEqual(resp.status_code, 200)

    def test_search_view(self):
        resp = self.client.get(reverse('articles:search'))
        self.assertEqual(resp.status_code, 200)

    def test_about_view(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
