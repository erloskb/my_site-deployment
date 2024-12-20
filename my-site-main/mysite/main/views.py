from django.shortcuts import render, get_object_or_404
from .models import Movie, Game

# Create your views here.
from django.http import HttpResponse

def index(request): 
    movies = Movie.objects.all().order_by('title')[:2]  # Получить только первые 2 фильма
    games = Game.objects.all().order_by('title')[:2]  # Получить только первые 2 игры
    context = {
        'movies': movies,
        'games': games
    }
    return render(request, 'main/index.html', context)

def games(request):
    games = Game.objects.all().order_by('title') 
    context = {'games': games}
    return render(request, 'main/games.html', context)
    
def movies(request):
    movies = Movie.objects.all().order_by('title') 
    context = {'movies': movies}
    return render(request, 'main/movies.html', context)

def contacts(request): 
    return render(request, 'main/contacts.html')

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'main/movie_detail.html', {'movie': movie})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'main/game_detail.html', {'game': game})