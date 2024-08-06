from django.urls import path
from violoes import views

# teria que escrever algo como:
# http://dominio.com.br/
# http://dominio.com.br/violoes
urlpatterns = [
    path('', views.home, name='home_violoes'),
    path('digiorgio/', views.digiorgio, name='digiorgio'),
    path('gianinni/', views.gianinni, name='gianinni'),
    path('vazioAzul', views.vazioAzul, name='vazioAzul'),
]
