# Generated by Django 3.0.4 on 2020-05-12 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('views', models.PositiveIntegerField()),
                ('website', models.URLField()),
                ('display_order', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image_relative_path', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('website', models.URLField(blank=True, null=True)),
                ('work', models.CharField(max_length=128)),
                ('education', models.CharField(max_length=128)),
                ('skills', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('views', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['views'],
            },
        ),
        migrations.CreateModel(
            name='TrackRating',
            fields=[
                ('track_rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.PositiveIntegerField()),
                ('track_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.Track')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackFavorite',
            fields=[
                ('track_favorite_id', models.AutoField(primary_key=True, serialize=False)),
                ('track_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Track')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRating',
            fields=[
                ('material_rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.PositiveIntegerField()),
                ('material_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Material')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialFavorite',
            fields=[
                ('material_favorite_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Material')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='api.Track'),
        ),
    ]
