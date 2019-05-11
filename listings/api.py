from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .choices import price_choices, bedroom_choices, state_choices
from .serializers import ListingSerializer
from .models import Listing


# Listing Viewset
class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ListingSerializer

    def list(self, request):
        queryset = Listing.objects.order_by(
            '-list_date').filter(is_published=True)

        # Keywords
        keywords = request.GET and (
            'keywords' in request.GET) and request.GET['keywords']
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

        # City
        city = request.GET and (
            'city' in request.GET) and request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city)

        # State
        state = request.GET and (
            'state' in request.GET) and request.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)

        # Bedrooms
        bedrooms = request.GET and (
            'bedrooms' in request.GET) and request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)

        # Price
        price = request.GET and (
            'price' in request.GET) and request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price)

        pagintor = Paginator(queryset, 6)
        page = request.GET and (
            'page' in request.GET) and request.GET['page'] or 1
        page_listings = pagintor.get_page(page)
        serializer = ListingSerializer(page_listings, many=True)
        return Response({
            "data": serializer.data,
            "query": request.GET,
            "has_other_pages": page_listings.has_other_pages(),
            "has_previous": page_listings.has_previous(),
            "has_next": page_listings.has_next(),
            "range": list(page_listings.paginator.page_range),
            "totalresults": page_listings.paginator.count,
        })


# Choice API
class ChoiceAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, *args, **kwargs):
        return Response({
            'state_choices': state_choices,
            'bedroom_choices': bedroom_choices,
            'price_choices': price_choices,
        })
