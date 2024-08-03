from django.http import HttpResponse

#from django.shortcuts import render

# Create your views here.

def appVioloes(request):
    print('Violão 1')
    return HttpResponse('Violões de appVioloes em /appVioloes/view.py')
