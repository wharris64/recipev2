from recipebox.models import Author, Recipe
from django import forms
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

class AddAuthorForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput) 
    bio = forms.CharField(widget=forms.Textarea)

# class AddRecipeForm(forms.ModelForm):
#     def __init__(self,*args,**kwargs):
#         if kwargs.pop('isAdmin'):
#             self.fields = [
#             "title",
#             "author",
#             "description",
#             "time_required",
#             "instructions",
#             ]
#         else:
#             self.fields = [
#             "title",
#             "description",
#             "time_required",
#             "instructions",
#         ]
#         super(AddRecipeForm,self).__init__(*args, **kwargs)

#     class Meta:
#         fields = [
#             "title",
#             "description",
#             "time_required",
#             "instructions",
#         ]

class AddRecipeForm(forms.Form):
    def __init__(self,*args,**kwargs):
        isAdmin = kwargs.pop('isAdmin')
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        if isAdmin:
            self.fields['author'] = forms.ModelChoiceField(queryset=Author.objects.all())

    
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    time_required = forms.IntegerField()
    instructions = forms.CharField(widget=forms.Textarea)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class Edit(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'time_required', 'instructions']