from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={"message" : "message"}
    templet=loader.get_template("app/index.html")
    
    return HttpResponse(templet.render(context,request))