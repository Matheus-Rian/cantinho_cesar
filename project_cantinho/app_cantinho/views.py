from django.shortcuts import render
from .forms import OptionsVendinha
from .models import VendinhaController

def get_products_by_vendinha(name):
  vendinha = VendinhaController.get_vendinha_by_name(name=name)
  products = [product for product in vendinha.products.all()]
  return products

def get_result_by_form(request):
	if request.method == 'POST':
		form = OptionsVendinha(request.POST)
		if form.is_valid():
			option = form.cleaned_data['choices']
		if option == 'BRUM':
			result = 'Brum'
		elif option == 'TIRADENTES':
			result = 'Tiradentes'
		elif option == 'APOLLO':
			result = 'Apollo'
	else:
		form = OptionsVendinha()
		result = 'Apollo'

	return { 'form': form, 'result': result }

def index(request):
	form = get_result_by_form(request=request)
	return render(request, "home/index.html", {
		'form': form['form'],
		'products': get_products_by_vendinha(name=form['result'])
	})
