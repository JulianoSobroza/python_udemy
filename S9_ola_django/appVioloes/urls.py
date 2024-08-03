from django.urls import path
from appVioloes import views

# teria que escrever algo como:
# http://dominio.com.br/
# http://dominio.com.br/violoes
urlpatterns = [
    path('lugar_um', views.appVioloes),
]
