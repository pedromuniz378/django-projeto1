from . import views
from django.urls import path

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/<id>/", views.recipes, name="recipe"),
]
