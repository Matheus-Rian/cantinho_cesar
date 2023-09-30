from django.shortcuts import render
from .forms import OptionsVendinha
from .models import VendinhaController

def get_products_by_vendinha(name):
  vendinha = VendinhaController.get_vendinha_by_name(name=name)
  products = [product for product in vendinha.products.all()]
  return products

def index(request):
	if request.method == 'POST':
		form = OptionsVendinha(request.POST)
		if form.is_valid():
			opcao = form.cleaned_data['choices']
		if opcao == 'BRUM':
				resultado = 'Brum'
		elif opcao == 'TIRADENTES':
				resultado = 'Tiradentes'
		elif opcao == 'APOLLO':
				resultado = 'Apollo'
	else:
		form = OptionsVendinha()
		resultado = 'Apollo'

	return render(request, "home/index.html", {'form': form, 'products': get_products_by_vendinha(name=resultado)})
