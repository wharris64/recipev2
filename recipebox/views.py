from django.shortcuts import render
from django.http import HttpResponse
from recipebox.models import Recipe, Author


def index(request):
    html = "index.html"

    return render(request, html)


def recipe(request, key_id):
    recipe_obj = Recipe.objects.get(pk=key_id)
    recipe = "recipe.html"

    return render(request, recipe, {"recipe": recipe_obj, "pk": recipe_obj.author.pk})


def author(request, key_id):
    author_obj = Author.objects.get(pk=key_id)
    author = "author.html"

    return render(request, author, {"author": author_obj})


def recipes(request):
    recipes_list = [x for x in Recipe.objects.all()]
    books = "recipes.html"

    return render(request, books, {"recipes": recipes_list})


def authors(request):
    authors_list = [x for x in Author.objects.all()]
    authors = "authors.html"

    return render(request, authors, {"authors": authors_list})
