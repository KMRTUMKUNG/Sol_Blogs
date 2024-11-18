from django.urls import path
from .views import index , about , register , Login

urlpatterns = [
    path('', index),
    path('about',about),
    path('Register',register),
    path('login_sol',Login)
]
