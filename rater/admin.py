from django.contrib import admin
from .models import Movie
from .models import Rating
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Movie, MovieAdmin)
class RatingAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Rating, RatingAdmin)

  


