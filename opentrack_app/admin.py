from django.contrib import admin
from opentrack_app.models import User, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite

# Register your models here.
admin.site.register(User)
admin.site.register(Track)
admin.site.register(Material)
admin.site.register(TrackRating)
admin.site.register(MaterialRating)
admin.site.register(TrackFavorite)
admin.site.register(MaterialFavorite)