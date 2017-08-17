from django.contrib import admin

from .models import Tag, Article


class TagsArticleInline(admin.TabularInline):
    model = Article.tags.through


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('num_articles', 'name')
    list_editable = ('name',)
    inlines = [TagsArticleInline, ]

    def num_articles(self, obj):
        return obj.article_set.count()

    # num_articles.int = True


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # action on bottom
    actions_on_top = False
    actions_on_bottom = True
    # add
    search_fields = ('title', 'content')
    date_hierarchy = 'first_commit'
    list_filter = ('tags', )

    readonly_fields = ('views', 'likes', 'first_commit', 'last_modified')
    # list
    list_display = ('title', 'first_commit', 'last_modified', 'views', 'likes')
    # ordering = ('first_commit',)
    # filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'tags')
        }),
        ('Time', {
            'classes': ('collapse',),
            'fields': ('first_commit', 'last_modified'),
        }),
        ('More', {
            'fields': ('views', 'likes'),
        }),
    )
    list_per_page = 20
    list_max_show_all = 50
