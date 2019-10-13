from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'views/listings/listings.html')


def listing(request):
    return render(request, 'views/listings/listing.html')

def search(request):
    return render(request, 'views/listings/search.html')
