from django.contrib import admin
from typography.models import Hashtag, Publication, PublicationComment


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'text']
