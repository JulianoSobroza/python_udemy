from django.contrib import admin
from django.urls import path, include

# http://dominio.com.br/
# http://dominio.com.br/violoes
urlpatterns = [
    path('', include('home.urls')),
    path('violoes/', include('violoes.urls')),
    path('admin/', admin.site.urls),
]
