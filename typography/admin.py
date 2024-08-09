from django.contrib import admin
from typography.models import Category, Hashtag, Publication, PublicationComment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_hidden']


@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'text']
