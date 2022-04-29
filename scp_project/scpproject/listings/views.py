from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Listing

# Create your views here.
def index(request):
    # return HttpResponse("listings index")
    newest_listings = Listing.objects.order_by('-date_added')[:15]
    context = {'newest_listings': newest_listings}
    return render(request, 'listings/index.html', context)
    
def show(request, listing_id):
    try:
        listing = Listing.object.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404("Listing does not exist")
    return render(request, 'listings/show.html', {'listing': listing})
