from django.shortcuts import get_object_or_404, render
from .models import Snake


fake_comments = [
    {"author": "Mark", "text": "Ssssss!"},
]


def index(request):
    return render(request, "snekbook/index.html", {"snake_number": 2})


def detail(request, snake_id):
    message = None
    if request.method == "POST":
        message = "Thanks for liking this snake!"
    snake = get_object_or_404(Snake, pk=snake_id)
    return render(
        request,
        "snekbook/detail.html",
        {
            "snake": snake,
            "recommended_snakes": snake.recommended_snakes.all(),
            "message": message,
            "comments": fake_comments,
        },
    )
