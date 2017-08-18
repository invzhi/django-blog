from django.test import TestCase

from articles.models import Article, Tag


class TagTest(TestCase):
    def setUp(self):
        Tag.objects.create(name='tag1')

    def test_get_absolute_url(self):
        tag = Tag.objects.get(name='tag1')
        self.assertEqual(
            tag.get_absolute_url(),
            '/articles/tagged/%s/' % tag.name
        )


class ArticleTest(TestCase):
    def setUp(self):
        Article.objects.create(
            title='article1',
            content='Hello Django\nThis is a article for django development.'
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(title='article1')
        self.assertEqual(
            article.get_absolute_url(),
            '/articles/%s/' % article.id
        )

    def test_article_summary(self):
        article = Article.objects.get(title='article1')
        self.assertEqual(article.summary(), 'Hello Django')
