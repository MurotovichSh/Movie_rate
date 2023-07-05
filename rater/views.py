from . import models,forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    movies=models.Movie.objects.all()
    return render(request, "rater/index.html",{"movies":movies})

def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    ratings = Rating.objects.filter(movie=movie)
    avg_rating = ratings.aggregate(models.Avg('value'))['value__avg']
    context = {'movie': movie, 'ratings': ratings, 'avg_rating': avg_rating}
    return render(request, 'rater/movie_detail.html', context)
def update_avg_rating(movie):
    ratings = Rating.objects.filter(movie=movie)
    avg_rating = ratings.aggregate(models.Avg('value'))['value__avg']
    movie.avg_rating = avg_rating
    movie.save()
@login_required(login_url='login')
def rate_movie_view(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        if rating_value is not None:
            try:
                rating = Rating.objects.create(
                    user=request.user,
                    movie=movie,
                    value=rating_value,
                )
            except IntegrityError:
                # If user has already rated this movie
                error_message = 'You have already rated this movie.'
                return render(request, 'rater/rate_movie.html', {'movie': movie, 'error_message': error_message})
            update_avg_rating(movie)
            return HttpResponseRedirect(reverse('movie_detail', args=[movie_id]))
    return render(request, 'rater/rate_movie.html', {'movie': movie})
def signup_view(request):
    userForm=forms.UserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.UserForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
        return redirect('login')
    return render(request,'accounts/signup.html',context=mydict)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def profile_view(request):
    return render(request, 'accounts/profile.html')
def user_view(request):
    movies=models.Movie.objects.all()
    return render(request, "rater/user.html",{"movies":movies})


    



    

