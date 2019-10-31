from django.contrib import admin
from django.urls import path
from recipebox import views
from recipebox.models import Recipe, Author

admin.site.register(Recipe)
admin.site.register(Author)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('authors', views.authors, name='authors'),
    path('recipes', views.recipes, name='recipes'),
    path('addrecipe/', views.add_recipe, name='recipe'),
    path('addauthor/', views.add_author, name='recipe'),
    path('author/<int:key_id>/', views.author, name='author'),
    path('recipe/<int:key_id>/', views.recipe, name='recipe'),
]
