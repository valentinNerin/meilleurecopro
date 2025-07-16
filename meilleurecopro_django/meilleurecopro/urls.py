from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stats_form/", views.stats_form, name="stats_form"),
    path("stats_results", views.stats_results, name="stats_results"),
]