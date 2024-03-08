from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required # gestion des utillisateur connecter
def index(request):
    context={"message" : "Bien venu dans la page principale"}
    templet=loader.get_template("app/index.html")
    
    return HttpResponse(templet.render(context,request))