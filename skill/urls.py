from django.urls import path
from .views import img , home

urlpatterns=[
    path("" , home , name='home'),
    path("img/" ,img , name='img'),
]