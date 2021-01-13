from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:id>', views.ver_contato, name='ver_contato'),
    path('busca/', views.busca, name='busca'),
]