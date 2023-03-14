from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import HttpResponse


def home(req):
    recipes = Recipe.objects.all().order_by("-id")
    return render(
        req,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(req, category_id):
    print(category_id)
    recipes = Recipe.objects.filter(category__id=category_id).order_by("-id")
    return render(
        req,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def recipes(req, id):
    return render(
        req,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": make_recipe(),
            "is_detail_page": True,
        },
    )
