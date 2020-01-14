from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox.forms import AddAuthorForm, AddRecipeForm, LoginForm, Edit
from recipebox.models import Recipe, Author



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
    favorites = author_obj.favorites.all()
    author = "author.html"

    return render(request, author, {"author": author_obj, "recipes": recipes, "favorites":favorites})


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


@user_passes_test(lambda u: u.is_superuser)
def addauthor(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            Author.objects.create(
                user=u,
                name=data["name"],
                bio=data.get('bio'),
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def editrecipe(request, id):
    form = None
    html = "editrecipe.html"
    instance = Recipe.objects.get(pk=id)
    if request.user.is_staff or request.user.author == instance.author:
        form = Edit(instance=instance)
        if request.method == "POST":
            form = Edit(request.POST, instance=instance)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.author = instance.author
                # breakpoint()
                recipe.save()
                
            return HttpResponseRedirect(request.GET.get('next', '/'))
        return render(request, html, {'form':form}) 
    else:
        return HttpResponseRedirect('/')


  
    
@login_required
def addrecipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST, isAdmin=request.user.is_staff)
        if form.is_valid():
            print(dir(form))
            # p = form.save(commit=False)
            author=""
            if not request.user.is_staff:
                author = request.user.author
            data = form.cleaned_data
            print(data)
            Recipe.objects.create(
                title=data["title"],
                author=data.get('author', author),
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"],
            )
            # p.save()

            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm(isAdmin=request.user.is_staff)

    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if user:= (
                    authenticate(
                        username=data["username"],
                        password=data["password"]
                    )
                ):
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next',reverse('homepage'))
                )

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def favorite(request, id):
    targeted_recipe = Recipe.objects.filter(id=id).first()
    # breakpoint()
    request.user.author.favorites.add(targeted_recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    