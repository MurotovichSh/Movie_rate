from django import forms
from django.contrib.auth.models import User
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }  
class MovieForm(forms.ModelForm):
    class Meta:
        model=models.Movie
        fields=['title','description','movie_image']
class RatingForm(forms.ModelForm):
    class Meta:
        model=models.Rating
        fields=['value']  





      