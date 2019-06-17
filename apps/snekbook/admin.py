from django.contrib import admin
from .models import Snake, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class SnakeAdmin(admin.ModelAdmin):
    model = Snake
    inlines = [CommentInline]


admin.site.register(Snake, SnakeAdmin)
admin.site.register(Comment)
