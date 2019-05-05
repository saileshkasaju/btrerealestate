from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  pagintor = Paginator(listings, 2)
  page = request.GET.get('page')
  page_listings = pagintor.get_page(page)
  context = {
    'listings': page_listings
  }
  return render(request, 'listings/listings.html', context)

def search(request):
  return render(request, 'listings/search.html')

def listing(request, listing_id):
  return render(request, 'listings/listing.html')