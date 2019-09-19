from django.http import HttpResponse 
from django.shortcuts import render
# Create your views here.
def productView(*args, **kwargs):
    return HttpResponse("<h1>product list</h1>")