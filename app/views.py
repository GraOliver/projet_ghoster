from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required
def index(request):
    context={"message" : "Bien venu dans la page principale"}
    templet=loader.get_template("app/index.html")
    
    return HttpResponse(templet.render(context,request))