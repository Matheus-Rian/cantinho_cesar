from django.shortcuts import render
from .models import VendinhaController

def get_products_by_vendinha(name):
  vendinha = VendinhaController.get_vendinha_by_name(name=name)
  products = [v for v in vendinha.products.all()]
  context = {
    "products": products,
  }
  return context

def index(request):
  return render(request, "home/index.html", get_products_by_vendinha(name="Apollo"))

