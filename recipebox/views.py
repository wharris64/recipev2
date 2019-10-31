from django.shortcuts import render
from django.http import HttpResponse
from recipebox.models import Recipe, Author
from recipebox.forms import AddAuthor, AddRecipe


def index(request):
    html = "index.html"
    recipe_list = Recipe.objects.all()

    return render(request, html, {"recipes": recipe_list})


def recipe(request, key_id):
    recipe_obj = Recipe.objects.get(pk=key_id)
    recipe = "recipe.html"

    return render(request, recipe, {"recipe": recipe_obj, "pk": recipe_obj.author.pk})


def author(request, key_id):
    author_obj = Author.objects.get(pk=key_id)
    recipes = [x for x in Recipe.objects.filter(author=author_obj)]
    author = "author.html"

    return render(request, author, {"author": author_obj, "recipes": recipes})


def recipes(request):
    recipes_list = [x for x in Recipe.objects.all()]
    recipes = "recipes.html"

    return render(request, recipes, {"recipes": recipes_list})


def authors(request):
    authors_list = [x for x in Author.objects.all()]
    auth_arr = []
    for auth in authors_list:
        obj = {}
        obj["author"] = auth
        recipes = Recipe.objects.filter(author=auth)
        obj["recipes"] = recipes
        auth_arr.append(obj)
    authors = "authors.html"

    return render(request, authors, {"authors": auth_arr})


def add_author(request):
    if request.method == "POST":
        form = AddAuthor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            form.save()
        
    form = AddAuthor()
    return render(request, 'generic_form.html', {'form':form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            form.save()

    form = AddRecipe()

    return render(request, 'generic_form.html', {'form':form})
