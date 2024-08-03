from django.urls import path

from . import views

# teria que escrever algo como:
# http://dominio.com.br/
# http://dominio.com.br/home
urlpatterns = [
    path('', views.home),
]
