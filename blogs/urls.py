from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('about',views.about),
    path('Register',views.register),
    path('login_sol',views.Login),
    path('all_Pro',views.All),
    path('apply_work',views.apply),
    path('Add_pro',views.add),
    path('pro_progress',views.progress),
    path('profile',views.profile),
    path('Sol_history',views.history),
]
