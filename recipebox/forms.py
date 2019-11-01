from recipebox.models import Author, Recipe
from django import forms

class AddAuthorForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    bio = forms.CharField(widget=forms.Textarea)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "author",
            "description",
            "time_required",
            "instructions",
        ]
