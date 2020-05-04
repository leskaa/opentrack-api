from django.shortcuts import render
from rest_framework import viewsets
from api.models import Profile, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite
from api.serializers import ProfileSerializer, TrackSerializer, MaterialSerializer, TrackRatingSerializer, MaterialRatingSerializer, TrackFavoriteSerializer, MaterialFavoriteSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


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
