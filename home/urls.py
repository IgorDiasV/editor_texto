from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvarrr/', views.salvar, name='salvar')
]
