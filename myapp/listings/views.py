from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .choices import bedroom_choices, price_choices, state_choices
from .models import Listings


# Create your views here.


def index(request):
    # listings = Listings.objects.all() #retreive all data available in Listing table

    listings = Listings.objects.order_by('-list_date').filter(
        is_published=True)  # order by list date in descending order and must be published

    # Implementing pagination in django
    paginator = Paginator(listings, per_page=6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    # Passing the additional data to related template page and can be retrieved using the dict key name
    context = {
        'listings': paged_listing
    }
    return render(request, template_name='pages/../listings/listings.html', context=context)


def listing(request, listing_id):
    # Directly redirect to not found page if Object not found
    listing = get_object_or_404(Listings, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, template_name='pages/../listings/listing.html', context=context)


def search(request):
    query_set_list = Listings.objects.order_by('-list_date')

    print(f'request params  :{request.GET}')

    # keyword (It is available in input field name of the form)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # It will search anywhere in the table col name here 'description' is col name
            query_set_list = query_set_list.filter(description__contains=keywords)

    # city (It is available in input field name of the form)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # exactly matches in the table col name here 'city' is col name
            query_set_list = query_set_list.filter(city__iexact=city)

    # State search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # exactly matches in the table col name here 'state' is col name
            query_set_list = query_set_list.filter(state__iexact=state)

    # Bedroom search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # matches less than and equal to in 'bedrooms' is col name
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # Bedroom search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # matches less than and equal to in 'price' is col name
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': query_set_list,
        'values': request.GET

    }
    return render(request, template_name='pages/../listings/search.html', context=context)
