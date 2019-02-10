from django.urls import path
from . import views

urlpatterns=[
    
    path("", views.index, name="index"),
    path("account", views.account, name="account"),
    path("event", views.event, name="event"),
    path("map", views.map, name="map"),
]
