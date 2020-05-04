from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profiles', views.ProfileView)
router.register('tracks', views.TrackView)
router.register('materials', views.MaterialView)
router.register('track_ratings', views.TrackRatingView)
router.register('material_ratings', views.MaterialRatingView)
router.register('track_favorites', views.TrackFavoriteView)
router.register('material_favorites', views.MaterialFavoriteView)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
