from django.urls import path, include
from knox import views as knox_views

from . import views
from .api import InquiryAPI

urlpatterns = [
    path('api/contacts', include('knox.urls')),
    path('api/contacts/inquiry', InquiryAPI.as_view()),
    path('contacts/contact', views.contact, name='contact'),
]
