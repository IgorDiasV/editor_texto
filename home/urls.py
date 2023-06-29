from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.salvar, name='salvar'),
    path('textos_salvos/', views.textos_salvos, name='textos_salvos')
]
