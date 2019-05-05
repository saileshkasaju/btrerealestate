from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  pagintor = Paginator(listings, 6)
  page = request.GET.get('page')
  page_listings = pagintor.get_page(page)
  context = {
    'listings': page_listings
  }
  return render(request, 'listings/listings.html', context)

def search(request):
  return render(request, 'listings/search.html')

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context)