from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from django.contrib.auth import get_user_model


from .models import Snake, Comment
from .forms import CommentForm


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
    num_snakes_per_row = 4
    num_results = num_snakes_per_row * 2

    def grouped(l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]
    
    return render(
        request,
        "snekbook/list.html",
        {
            "snake_groups": grouped(snakes[cursor : cursor + num_results], 4),
            "cursor_left_enabled": cursor - num_results < 0,
            "cursor_left": cursor - num_results if 0 < cursor - num_results else 0,
            "cursor_right_enabled": True,
            "cursor_right": cursor + num_results,
        },
    )


def detail(request, snake_id):
    snake = get_object_or_404(Snake, pk=snake_id)
    if request.method == "POST":
        if '__comment__' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment(
                    snake=snake,
                    author=request.user,
                    text=form.cleaned_data['comment'],
                ).save()
    else:
        form = CommentForm()
    return render(
        request,
        "snekbook/detail.html",
        {
            "snake": snake,
            "recommended_snakes": snake.recommended_snakes.all()[:8],
            "likes": snake.likers.count(),
            "comments": snake.comments.all(),
            "form": form,
        },
    )


def like_snake(request, snake_id, redirect_url):
    snake = get_object_or_404(Snake, pk=snake_id)
    request.user.snake_set.add(snake)
    return redirect(f"/{redirect_url}/{snake_id}")


def unlike_snake(request, snake_id, redirect_url):
    snake = get_object_or_404(Snake, pk=snake_id)
    request.user.snake_set.remove(snake)
    return redirect(redirect_url)