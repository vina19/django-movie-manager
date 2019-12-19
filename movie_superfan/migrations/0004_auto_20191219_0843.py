# Generated by Django 2.1.11 on 2019-12-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_superfan', '0003_movie_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite_movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_superfan.Movie'),
        ),
    ]