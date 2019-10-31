from recipebox.models import Author
from django import forms

class AddAuthor(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    bio = forms.CharField(widget=forms.Textarea)

class AddRecipe(forms.Form):
    title = forms.CharField(max_length=64)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=64)
    time_required = forms.IntegerField()
    instructions = forms.CharField(widget=forms.Textarea)
