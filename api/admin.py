from django.contrib import admin
from .models import Profile, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite

admin.site.register(Profile)
admin.site.register(Track)
admin.site.register(Material)
admin.site.register(TrackRating)
admin.site.register(MaterialRating)
admin.site.register(TrackFavorite)
admin.site.register(MaterialFavorite)
