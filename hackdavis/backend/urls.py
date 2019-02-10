from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("create", views.create_user, name="create"),
    path("event", views.event, name="event"),
    path("map", views.map, name="map"),
]
