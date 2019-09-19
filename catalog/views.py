from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def catalogView(*args, **kwargs):
    return HttpResponse("<h1>Catalog product</h1>")