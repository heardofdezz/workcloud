from django.contrib import admin

from . import models


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_active',
        'permission_read',
        'permission_write',
        'permission_reply',
    )
    search_fields = (
        '-id',
    )
    ordering = (
        '-id',
    )
    list_display_links = (
        'id',
    )


@admin.register(models.Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'title',
        'created_at',
    )
    search_fields = (
        'name',
        'title',
        'description',
    )
    ordering = (
        '-id',
    )
    list_display_links = (
        'id',
        'name',
        'title',
    )


@admin.register(models.Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'forum',
        'title',
        'user',
        'is_deleted',
        'created_at',
        'modified_at',
    )
    search_fields = (
        'title',
        'content',
    )
    ordering = (
        '-id',
    )
    list_display_links = (
        'id',
        'title',
    )


@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'thread',
        'reply_id',
        'user',
        'content',
        'is_deleted',
        'modified_at',
    )
