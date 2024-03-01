from django.contrib.auth import forms
from django import forms as form_avant
from django.contrib.auth import get_user_model

class LoginUser(form_avant.Form):
    pass

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model=get_user_model()
        fields="__all__"
    

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model=get_user_model()