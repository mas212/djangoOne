from django.http import HttpResponse 
from django.shortcuts import render
# Create your views here.
def product(request, *args, **kwargs):
    #return HttpResponse("<h1>product list</h1>")
    data = {
        'name' : 'room delux',
        'price' : 300,
        'fasilities' : ['wifi', 'print', 'eat']
    }
    return render(request, "product.html", data)