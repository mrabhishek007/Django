from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    # return HttpResponse('<h1>My Home Page</h1>') # returns static markup
    return render(request, 'views/index.html')


def about(request):
    return render(request, 'views/about.html')