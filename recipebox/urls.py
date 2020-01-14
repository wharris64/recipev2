from django.contrib import admin
from django.urls import path
from recipebox import views
from recipebox.models import Recipe, Author

admin.site.register(Recipe)
admin.site.register(Author)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="homepage"),
    path('authors/', views.authors, name='authors'),
    path('recipes/', views.recipes, name='recipes'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addrecipe/', views.addrecipe, name='recipe'),
    path('addauthor/', views.addauthor, name='recipe'),
    path('author/<int:key_id>/', views.author, name='author'),
    path('recipe/<int:key_id>/', views.recipe, name='recipe'),
    path('editticket/<int:id>/', views.editrecipe),
    path('favorite/<int:id>/', views.favorite, name='favorite')

]
