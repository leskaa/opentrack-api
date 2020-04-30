from django.urls import path, include
from opentrack_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('tracks', views.TrackView)
router.register('materials', views.MaterialView)
router.register('track_ratings', views.TrackRatingView)
router.register('material_ratings', views.MaterialRatingView)
router.register('track_favorites', views.TrackFavoriteView)
router.register('material_favorites', views.MaterialFavoriteView)

urlpatterns = [
    path('', include(router.urls))
]
