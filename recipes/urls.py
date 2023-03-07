from recipes.views import home, about, contact
from django.urls import path

urlpatterns = [
    path("", home),
    path("sobre/", about),
    path("contato/", contact),
]
