from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    # DateTime
    first_commit = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:self.content.find('\n')]

    def reading_time(self):
        return len(self.content) // 1000
