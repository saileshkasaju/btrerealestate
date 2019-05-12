from rest_framework import routers
from django.urls import path

from . import views
from .api import ChoiceAPI, ListingViewSet


router = routers.DefaultRouter()
router.register('api/listings', ListingViewSet, 'listings')

urlpatterns = router.urls + [
    path('api/listing/search-choices', ChoiceAPI.as_view()),
    path('listings/', views.index, name="listings"),
    path('listings/<int:listing_id>', views.listing, name="listing"),
    path('listings/search', views.search, name="search"),
]
