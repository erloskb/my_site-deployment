# Generated by Django 5.1.1 on 2024-11-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('original_title', models.CharField(blank=True, max_length=200, null=True)),
                ('cover_image', models.ImageField(upload_to='game_covers/')),
                ('trailer_url', models.URLField(blank=True, null=True)),
                ('release_year', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('plot', models.TextField()),
                ('themes', models.CharField(max_length=200)),
                ('visual_style', models.CharField(max_length=200)),
                ('music', models.CharField(max_length=200)),
                ('awards', models.TextField(blank=True, null=True)),
                ('legacy', models.TextField(blank=True, null=True)),
                ('wikipedia_url', models.URLField(blank=True, null=True)),
                ('characters', models.ManyToManyField(blank=True, related_name='games', to='main.character')),
            ],
        ),
    ]
