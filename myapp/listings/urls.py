from django.urls import path
from . import views

# /listings is default url mentioned in myapp urls.py

urlpatterns = [
    path('', views.index, name='listings'),  # /listing
    path('<int:listing_id>', views.listing, name='listing'),  # /listing/id
    path('search', views.search, name='search')  # /listing/search
]
