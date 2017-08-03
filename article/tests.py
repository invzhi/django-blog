from django.test import TestCase
from .models import Article


class ArticleModelTests(TestCase):

    def setUp(self):
        Article.objects.create(title='article1',
                               content='Hello Django\nThis is a article for django development.')

    def test_article_summary(self):
        article = Article.objects.get(title='article1')
        self.assertEqual(article.summary(), 'Hello Django')
