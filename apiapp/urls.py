from django.db import models
from django.urls import path
from . import views

app_name = "apiapp"

urlpatterns = [
    path('route', views.route, name="route"),
    path('map', views.map, name="map"),
]