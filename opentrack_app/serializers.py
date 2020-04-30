from rest_framework import serializers
from opentrack_app.models import User, Track, Material, TrackRating, MaterialRating, TrackFavorite, MaterialFavorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('usr_id', 'usr_username', 'usr_password_hash', 'usr_email', 'usr_location', 'usr_website', 'usr_work', 'usr_education', 'usr_skills')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('trk_id', 'trk_title', 'trk_description', 'trk_views', 'trk_author')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('mtr_id', 'mtr_title', 'mtr_description', 'mtr_views', 'mtr_website', 'mtr_track', 'mtr_display_order')

class TrackRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackRating
        fields = ('tr_id', 'tr_rating', 'tr_usr_fk', 'tr_trk_fk')

class MaterialRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRating
        fields = ('mr_id', 'mr_rating', 'mr_usr_fk', 'mr_mtr_fk')
    
class TrackFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackFavorite
        fields = ('tf_id', 'tf_usr_fk', 'tf_trk_fk')

class MaterialFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialFavorite
        fields = ('mf_id', 'mf_usr_fk', 'mf_mtr_fk')
