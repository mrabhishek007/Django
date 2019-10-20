from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'listing', 'email', 'contact_date')  # Add extra table field in the listing page
    list_display_links = ('id', 'name')  # Adding extra functionality to redirect the links in listing page
    search_fields = ('name', 'listing', 'email')  # Adding search functionality on given fields
    list_per_page = 25  # Adding Pagination


admin.site.register(Contact, ContactAdmin)
