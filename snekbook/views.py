from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from django.contrib.auth import get_user_model
from .models import Snake, Comment


def index(request):
    return render(request, "snekbook/index.html")


def profile(request, user_id):
    this_user = get_object_or_404(get_user_model(), pk=user_id)
    return render(
        request,
        "snekbook/profile.html",
        {
            "snakes": request.user.snake_set.all(),
            "thisuser": this_user,
            "allow_deletes": this_user == request.user,
        },
    )


def list(request, cursor):
    snakes = Snake.objects.all()
    num_snakes = Snake.objects.count()
    num_results = 15
    return render(
        request,
        "snekbook/list.html",
        {
            "snakes": snakes[cursor : cursor + num_results],
            "cursor_left": None if cursor == 0 else cursor - num_results,
            "cursor_right": None
            if num_snakes < cursor + num_results
            else cursor + num_results,
        },
    )


def detail(request, snake_id):
    snake = get_object_or_404(Snake, pk=snake_id)
    return render(
        request,
        "snekbook/detail.html",
        {
            "snake": snake,
            "recommended_snakes": snake.recommended_snakes.all(),
            "likes": snake.likers.count(),
            "comments": snake.comments.all(),
        },
    )


def like_snake(request, snake_id):
    snake = get_object_or_404(Snake, pk=snake_id)
    request.user.snake_set.add(snake)
    return redirect(f"/detail/{snake_id}")


def unlike_snake(request, snake_id):
    snake = get_object_or_404(Snake, pk=snake_id)
    request.user.snake_set.remove(snake)
    return redirect(f"/profile/{request.user.pk}")


def comment_snake(request, snake_id):
    new_comment = Comment(
        snake=get_object_or_404(Snake, pk=snake_id), author=request.user, text="???"
    ).save()
    return redirect(f"/detail/{snake_id}")
