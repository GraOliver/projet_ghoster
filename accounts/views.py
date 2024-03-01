from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginUser,UserChangeForm,UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
# Create your views here.
message_erreur ="Identifiant ou mot de passe incorecte"

def login_app(request): # connexion du client
    if request.method =='POST': # au clique on recupeur les données dans les champ
        username =request.POST["username"]
        password =request.POST["password"]
        user =authenticate(request,username=username,password =password) # verification des valeur entrer par
        
        if user is not None :
            return redirect("app:indexOfApp")
        else :
            messages.info(request,message_erreur)    
            
    return render(request,"accounts/login.html",{"message":AuthenticationForm()})



def logout_app(request):
    logout(request)
    return redirect("accounts:login")

def register_app(request):
    if request.method=='POST':
        pass
    
    form = UserCreationForm()
    return render(request,"accounts/register.html",{"form":form}) 

def pass_forgeted(request):
    form =UserChangeForm()
    return render(request,"accounts/pass_forgeted.html",{"form":form})
