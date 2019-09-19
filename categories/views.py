from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def categori_view(request, *args, **kwargs):
    #return HttpResponse("<h1>categori page</h1>")
    return render(request, "categori.html", {})