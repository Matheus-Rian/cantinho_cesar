from django.shortcuts import render
from .models import VendinhaController

def index(request):
  vendinha = VendinhaController.get_vendinha_by_name(name="Apollo")
  output = [v for v in vendinha.products.all()]
  context = {
      "data": output,
  }
  return render(request, "home/index.html", context)
