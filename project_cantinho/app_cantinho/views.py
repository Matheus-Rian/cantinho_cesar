from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import OptionsVendinha
from .models import VendinhaController, Product, CartController
from django.views import View
from .models import Product , UserProfile 
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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

class Cart(View):
	def get(self, request, product_id, *args, **kwargs):
		product_id = int(product_id)
		product = get_object_or_404(Product, pk=product_id)
		CartController.add_to_cart(product=product)
		return HttpResponse(f"{product.name} adicionado ao carrinho!")

def index(request):
	form = get_result_by_form(request=request)
	return render(request, "home/index.html", {
		'form': form['form'],
		'products': get_products_by_vendinha(name=form['result'])
	})

def listar_produtos(request):
    produtos = Product.objects.all()
    return render(request, 'products/index.html', {'products': produtos})

def pagina_de_cadastro(request):
    return render(request, "cadastro/cadastro.html")

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
        if usuario_aux:
            return render(request, 'cadastro/cadastro.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})
    except User.DoesNotExist:
        nome_usuario = request.POST['nome-usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        UserProfile.objects.create(user=novoUsuario)
        login(request, novoUsuario)
        return HttpResponseRedirect("/")
    