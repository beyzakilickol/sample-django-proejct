from django.shortcuts import render
from .models import Game

# Create your views here.
# views.py knows to look at the templates folder so we do not need to include templates in the path


def home(request):
    print('printing home request', request)
    return render(request, "firstapp/home.html",
                  {"numberOfGames": Game.objects.count()}
                  )


def test(request):
    print(request)
    return render(request, 'firstapp/test.html')