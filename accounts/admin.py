from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm,UserChangeForm

admin.site.register(User,UserAdmin)
class UserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=User
    