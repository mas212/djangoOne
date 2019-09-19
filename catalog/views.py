from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def catalog(request, *args, **kwargs):
    return render(request, "catalog.html")