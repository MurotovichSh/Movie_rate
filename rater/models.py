from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    movie_image=models.ImageField(upload_to="movie_image/",null=False, blank=False)
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    value=models.IntegerField()
    class Meta:
        unique_together = ('user', 'movie')
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
     