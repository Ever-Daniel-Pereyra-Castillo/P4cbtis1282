from django.shortcuts import render
# Create your views here.

def index(request):
    '''Esto es la página principal'''
    return render(request, "index.html")