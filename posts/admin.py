from django.contrib import admin

from .models import Post, Commit


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'create_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'create_at')


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('creator', 'post_id', 'create_at')
    search_fields = ('content',)
    list_filter = ('post', 'create_at')
