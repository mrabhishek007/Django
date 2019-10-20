from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    # return HttpResponse('<h1>My Home Page</h1>') # returns static markup

    listings = Listings.objects.order_by('-list_date').filter(
        is_published=True)[0:3]  # order by list date in descending order and must be published

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request, template_name='pages/index.html', context=context)


def about(request):
    # Get all realtor
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'mvp_realtors': mvp_realtors,
        'realtors': realtors
    }

    return render(request, template_name='pages/about.html', context=context)
