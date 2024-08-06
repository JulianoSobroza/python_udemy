from django.shortcuts import render

# Create your views here.
def home(request):
    print('Violão home')
    return render(
        request,
        #'violao/home.html'
        'violoes/home.html'
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
