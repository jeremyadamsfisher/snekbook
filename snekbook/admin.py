from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Snake, Comment, User

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class SnakeAdmin(admin.ModelAdmin):
    model=Snake
    inlines = [CommentInline]

class CustomUserAdmin(UserAdmin):
    model = User

admin.site.register(User, CustomUserAdmin)
admin.site.register(Snake, SnakeAdmin)
admin.site.register(Comment)