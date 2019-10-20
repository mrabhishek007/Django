from django.urls import path
from . import views

# /listings is default url mentioned in myapp urls.py

urlpatterns = [
    path('login', views.login, name='login'),  # /login
    path('register', views.register, name='register'),  # /register
    path('dashboard', views.dashboard, name='dashboard'),  # /dashboard
    path('logout', views.logout, name='logout'),  # /logout
]
