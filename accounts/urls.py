from django.urls import path
from .import views

urlpatterns = [
    path('registerUser/',views.registerUser,name='registerUser'),
    #path('register/',views.user()),
]
