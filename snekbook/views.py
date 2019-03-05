from django.shortcuts import render


def index(request):
    snakes = [
        {"name": "Boa Constrictor", "stars": 3},
        {"name": "Sneky snek", "stars": 4}
    ]
    return render(request, "snekbook/index.html", {"snake_number": len(snakes), "snakes": snakes})
