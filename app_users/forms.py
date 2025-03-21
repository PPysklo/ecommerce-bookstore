from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput, EmailInput

from .models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)

        for name,field  in self.fields.items():
            if name != 'password':
                field.widget.attrs.update({'placeholder' : name.capitalize()})
        
        self.fields['email'].widget = EmailInput(attrs={'placeholder': ""})
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': ''})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': ''})
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'city', 'address', 'postal_code', 'country', 'telephone']          

