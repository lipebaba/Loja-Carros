from django.http import JsonResponse
from .models import Carro

def listar_carros(request):
    carros = Carro.objects.all().values()
    return JsonResponse(list(carros), safe=False)

def carros_disponiveis(request):
    carros = Carro.objects.filter(status='DISPONIVEL').values()
    return JsonResponse(list(carros), safe=False)