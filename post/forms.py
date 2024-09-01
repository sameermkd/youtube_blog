from django import forms
from . models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MakePost(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2','first_name', 'last_name')
        help_texts = {
            'username':None,
            'emai':None
        }
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''