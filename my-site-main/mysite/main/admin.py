from django.contrib import admin
from .models import Movie, Game, Character, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year')
    search_fields = ('title', 'director')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie', 'created_at')
    search_fields = ('name', 'movie__title')

@admin.register(Game)  # Исправлено: зарегистрируем Game корректно
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'release_year')
    search_fields = ('title', 'developer')