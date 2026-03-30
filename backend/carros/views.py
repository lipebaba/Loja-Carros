from django.http import JsonResponse
from .models import Carro

def listar_carros(request):
    carros = Carro.objects.all().values()
    return JsonResponse(list(carros), safe=False)