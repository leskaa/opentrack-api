from django.db import models

# Create your models here.

class User(models.Model):
    usr_id = models.AutoField(primary_key = True)
    usr_username = models.CharField(max_length = 32, unique = True)
    usr_password_hash = models.CharField(max_length = 64)
    usr_email = models.EmailField(unique = True)
    usr_location = models.CharField(max_length = 64)
    usr_website = models.URLField(null = True)
    usr_work = models.CharField(max_length = 64)
    usr_education = models.CharField(max_length = 64)
    usr_skills = models.CharField(max_length = 256)

    def __str__(self):
        return self.usr_username

class Track(models.Model):
    trk_id = models.AutoField(primary_key = True)
    trk_title = models.CharField(max_length = 32)
    trk_description = models.CharField(max_length = 256)
    trk_views = models.PositiveIntegerField()
    trk_author = models.ForeignKey(User, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return self.trk_title

class Material(models.Model):
    mtr_id = models.AutoField(primary_key = True)
    mtr_title = models.CharField(max_length = 32)
    mtr_description = models.CharField(max_length = 32)
    mtr_views = models.PositiveIntegerField()
    mtr_website = models.URLField(null = False)
    mtr_track = models.ForeignKey(Track, on_delete = models.CASCADE, null = False)
    mtr_display_order = models.PositiveIntegerField()

    def __str__(self):
        return self.mtr_title

class TrackRating(models.Model):
    tr_id = models.AutoField(primary_key = True)
    tr_rating = models.PositiveIntegerField()
    tr_usr_fk = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    tr_trk_fk = models.ForeignKey(Track, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return str(self.tr_rating) + " : " + self.tr_trk_fk + " : " + self.tr_usr_fk

class MaterialRating(models.Model):
    mr_id = models.AutoField(primary_key = True)
    mr_rating = models.PositiveIntegerField()
    mr_usr_fk = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    mr_mtr_fk = models.ForeignKey(Material, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return str(self.mr_rating) + " : " + self.mr_mtr_fk + " : " + self.mr_usr_fk

class TrackFavorite(models.Model):
    tf_id = models.AutoField(primary_key = True)
    tf_usr_fk = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    tf_trk_fk = models.ForeignKey(Track, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return self.tf_trk_fk + " : " + self.tf_usr_fk

class MaterialFavorite(models.Model):
    mf_id = models.AutoField(primary_key = True)
    mf_usr_fk = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    mf_mtr_fk = models.ForeignKey(Material, on_delete = models.CASCADE, null = False)

    def __str__(self):
        return self.mf_mtr_fk + " : " + self.mf_usr_fk