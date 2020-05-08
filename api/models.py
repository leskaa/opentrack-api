from django.db import models
from users.models import CustomUser


class Profile(models.Model):
    user_id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    image_relative_path = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    website = models.URLField(blank=True, null=True)
    work = models.CharField(max_length=64)
    education = models.CharField(max_length=64)
    skills = models.CharField(max_length=256)


class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    views = models.PositiveIntegerField()
    author = models.ForeignKey(
        CustomUser, related_name='author', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['views']

    def __str__(self):
        return self.title


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    views = models.PositiveIntegerField()
    website = models.URLField(null=False)
    track = models.ForeignKey(
        Track, related_name='materials', on_delete=models.CASCADE, null=False)
    display_order = models.PositiveIntegerField()
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class TrackRating(models.Model):
    track_rating_id = models.AutoField(primary_key=True)
    rating = models.PositiveIntegerField()
    user_fk = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False)
    track_fk = models.ForeignKey(Track, on_delete=models.CASCADE, null=False)


class MaterialRating(models.Model):
    material_rating_id = models.AutoField(primary_key=True)
    rating = models.PositiveIntegerField()
    user_fk = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False)
    material_fk = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=False)


class TrackFavorite(models.Model):
    track_favorite_id = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False)
    track_fk = models.ForeignKey(Track, on_delete=models.CASCADE, null=False)


class MaterialFavorite(models.Model):
    material_favorite_id = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False)
    material_fk = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=False)
