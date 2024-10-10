from django.shortcuts import render

# Create your views here.

def ver_lista(request):
    return render(request,'index.html')