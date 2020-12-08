from django.contrib import admin
from .models import Favorites, Movie

# Register your models here.

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
