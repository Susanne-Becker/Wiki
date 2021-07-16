"""
Wiki

Encyclopedia website

Gemaakt door: Susanne Becker
"""

from django.urls import path

from . import views

"""
All the paths you can go to on the website
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newEntry", views.newEntry, name="newEntry"),
    path("wiki/<str:entry>/edit", views.edit, name="edit")
]
