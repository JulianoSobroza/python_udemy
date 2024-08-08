from django.shortcuts import render
from violoes.data import posts

# Create your views here.
def home(request):
    print('Violão home')
    return render(
        request,
        #'violao/home.html'
        'violoes/home.html'
        )

def index(request):
    print('Index do blog Violoes')
    
    context = {
        'text': 'Olá blog',
        'posts': posts
    }
    
    return render(
        request,
        'violoes/index.html',
        context
    )

def digiorgio(request):
    print('Violão Di Giorgio')
    return render(
        request,
        #'violao/digiorgio.html'
        'violoes/digiorgio.html'
        )

def gianinni(request):
    print('Violão Gianinni')
    return render(
        request,
        #'violao/gianinni.html'
        'violoes/gianinni.html'
        )


def vazioAzul(request):
    print('vazioAzul')
    return render(
        request,
        #'violao/gianinni.html'
        'violoes/vazioAzul.html'
        )
