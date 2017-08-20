from django.test import TestCase

from articles.models import Article, Tag


class TagTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='test_tag')

    def test_get_absolute_url(self):
        self.assertEqual(
            self.tag.get_absolute_url(),
            '/articles/tagged/%s/' % self.tag.name,
        )


class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(
            title='Test Article',
            content='Hello\nArticle for django test.',
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(),
            '/articles/%s/' % self.article.id,
        )

    def test_summary(self):
        self.assertEqual(self.article.summary(), 'Hello')
