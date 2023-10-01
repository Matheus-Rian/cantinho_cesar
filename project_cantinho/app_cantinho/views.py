from django.shortcuts import render, HttpResponse
from .forms import OptionsVendinha
from .models import VendinhaController
from django.views import View

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

class Cart(View):
	def get(self, request,product_id, *args, **kwargs):
		return HttpResponse("Método executado com sucesso!" + str(product_id))
