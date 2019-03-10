from django.shortcuts import render
from .models import Snake

def index(request):
    return render(
        request,
        "snekbook/index.html",
        {
            "snake_number": 2
        }
    )

def detail(request, snake_id):
    snake = Snake.objects.get(pk=snake_id)
    return render(
        request,
        "snekbook/detail.html",
        {
            "snake": snake,
            "recommended_snakes": snake.recommended_snakes.all()
        }
    )
