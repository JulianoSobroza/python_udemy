from django.http import HttpResponse

#from django.shortcuts import render

# Create your views here.
def home(request):
    print('home')
    return HttpResponse('Página Inicial de home em /home/views.py')