from django.contrib import admin

from .models import Listings


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'is_published', 'price', 'list_date', 'realtor')  # Add extra table field in the listing page
    list_display_links = ('id', 'title')  # Adding extra functionality to redirect the links in listing page
    list_filter = ('realtor',)  # Add filter in the Listing page
    list_editable = ('is_published',)  # directly update the table field in the Listing page
    search_fields = ('title', 'address', 'city', 'state', 'zipcode', 'description',
                     'price')  # Adding search functionality on given fields
    list_per_page = 25  # Adding Pagination


admin.site.register(Listings, ListingAdmin)
