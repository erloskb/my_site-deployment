from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для главной страницы
path('games/', views.games, name='games'),  # Маршрут для главной страницы

path('movies/', views.movies, name='movies'),  # Маршрут для главной страницы
path('contacts/', views.contacts, name='contacts'),  # Маршрут для главной страницы
 path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
  path('game/<int:game_id>/', views.game_detail, name='game_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)