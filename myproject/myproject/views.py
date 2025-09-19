# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # pass
    return render(request, 'home.html')

def about(request): 
    # pass
    return render(request, 'about.html')
