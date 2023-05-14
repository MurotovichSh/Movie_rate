from django.contrib import admin
from django.urls import path
from rater import views
from django.contrib.auth.views import LogoutView
"""
URL configuration for MovieRate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('movie_detail/<int:pk>/',views.movie_detail_view,name='movie_detail'),
    path('movie_rate/<int:movie_id>/',views.rate_movie_view,name='movie_rate'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='rater/logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('user',views.user_view, name='user')
]
