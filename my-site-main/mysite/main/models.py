from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    plot = models.TextField()
    themes = models.TextField()  # Можно использовать ManyToManyField для тем
    visual_style = models.TextField()
    music = models.TextField()
    awards = models.TextField()
    legacy = models.TextField()
    wikipedia_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/movies/')  # Не забудьте настроить MEDIA_URL и MEDIA_ROOT

    def __str__(self):
        return self.title

class Character(models.Model):
    movie = models.ForeignKey(Movie, related_name='characters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.movie}'
    
class Game(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(upload_to='game_covers/')
    trailer_url = models.URLField(max_length=200, blank=True, null=True)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    plot = models.TextField()
    themes = models.CharField(max_length=200)
    visual_style = models.CharField(max_length=200)
    music = models.CharField(max_length=200)
    awards = models.TextField(blank=True, null=True)
    legacy = models.TextField(blank=True, null=True)
    wikipedia_url = models.URLField(max_length=200, blank=True, null=True)

    characters = models.ManyToManyField(Character, related_name='games', blank=True)

    def __str__(self):
        return self.title