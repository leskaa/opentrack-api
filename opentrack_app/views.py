from django.shortcuts import render
from rest_framework import viewsets
from opentrack_app.models import User, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite
from opentrack_app.serializers import UserSerializer, TrackSerializer, MaterialSerializer, TrackRatingSerializer, MaterialRatingSerializer, TrackFavoriteSerializer, MaterialFavoriteSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class MaterialView(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class TrackRatingView(viewsets.ModelViewSet):
    queryset = TrackRating.objects.all()
    serializer_class = TrackRatingSerializer

class MaterialRatingView(viewsets.ModelViewSet):
    queryset = MaterialRating.objects.all()
    serializer_class = MaterialRatingSerializer

class TrackFavoriteView(viewsets.ModelViewSet):
    queryset = TrackFavorite.objects.all()
    serializer_class = TrackFavoriteSerializer

class MaterialFavoriteView(viewsets.ModelViewSet):
    queryset = MaterialFavorite.objects.all()
    serializer_class = MaterialFavoriteSerializer