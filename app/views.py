from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models


@login_required # gestion des utillisateur connecter
def index(request):
    context={"message" :"" }
    template="app/index.html"
    
    return render(request,template,context)