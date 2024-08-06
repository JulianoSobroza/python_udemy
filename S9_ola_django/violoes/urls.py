from django.urls import path
from violoes import views

# teria que escrever algo como:
# http://dominio.com.br/
# http://dominio.com.br/violoes
urlpatterns = [
    path('', views.home),
    path('digiorgio/', views.digiorgio),
    path('gianinni/', views.gianinni),
    path('vazioAzul', views.vazioAzul),
]
