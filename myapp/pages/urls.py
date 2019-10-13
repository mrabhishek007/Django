from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 'name' is the href link which will be used to redirect to this page
    path('about', views.about, name='about')
]
