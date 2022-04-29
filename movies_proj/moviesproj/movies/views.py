from django.shortcuts import render
from django.http import Http404

from .models import Movie

# Create your views here.
def index(request):
    # return HttpResponse("Movies index")
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'mewest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})