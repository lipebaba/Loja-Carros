from django.urls import path
from .views import listar_carros

urlpatterns = [
    path('carros/', listar_carros),
]