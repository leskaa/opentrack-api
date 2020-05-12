from django.shortcuts import render
from rest_framework import viewsets
from api.models import Profile, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite
from api.serializers import GetTrackSerializer, MaterialFavoriteSerializer, MaterialRatingSerializer, MaterialSerializer, ProfileSerializer, TrackFavoriteSerializer, TrackRatingSerializer, TrackSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetTrackSerializer
        return TrackSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views", ))
        return super().retrieve(request, *args, **kwargs)


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
