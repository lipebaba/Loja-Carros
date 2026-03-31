from django.urls import path
from .views import listar_carros
from . import views


urlpatterns = [
    path('carros/', listar_carros),
]

urlpatterns = [
    path('carros/', views.listar_carros),
    path('carros/disponiveis/', views.carros_disponiveis),
]   