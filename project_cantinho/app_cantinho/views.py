from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import OptionsVendinha
from .models import VendinhaController, Product, Cart,UserProfile,Favoritar, Pedido
from django.views import View
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .pagamento_utils import pagamento_com_cartao
import random, string, time

def get_products_by_vendinha(name):
  vendinha = VendinhaController.get_vendinha_by_name(name=name)
  products = [product for product in vendinha.products.all()]
  return products

def get_result_by_form(request):
	if request.method == 'POST':
		form = OptionsVendinha(request.POST)
		if form.is_valid():
			option = form.cleaned_data['Selecione']
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

@login_required
def cart_home(request,product_id):
    user = request.user
    carrinho, created = Cart.objects.get_or_create(user=user)
    produto = Product.objects.get(id=product_id)
    carrinho.products.add(produto)
    return HttpResponseRedirect("/carrinho/")

@login_required
def carrinho(request):
    user = request.user
    carrinho = Cart.objects.get(user=user)  
    products = carrinho.products.all()
    total = sum(product.value for product in products)
    
    return render(request, 'carrinho/carrinho.html', {'products': products, 'total': total})



index_page_html =  "app_cantinho/index.html"
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/menu/")
    else:
        return render(request, index_page_html)
    
def menu(request):
	form = get_result_by_form(request=request)
	return render(request, "menu/menu.html", {
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
        return HttpResponseRedirect("/menu/")

@require_POST
def entrar(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
    except User.DoesNotExist:
        messages.error(request, "Usuário não existe ou credenciais incorretas")
        return HttpResponseRedirect("/")
    
    usuario = authenticate(username=usuario_aux.username,password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/menu/')
    return HttpResponseRedirect("/")
    
@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def salvar_horario(request):
    if request.method == "POST":
        hora_retirada = request.POST.get("hora_retirada")
        user = request.user
        carrinho, created = Cart.objects.get_or_create(user=user)
        carrinho.hora_retirada = hora_retirada
        carrinho.save()
        messages.success(request, "Horário salvo com sucesso.")
        return redirect("/carrinho/")

    return render(request, "carrinho.html")


@login_required
def meus_favoritos(request):
    user = request.user
    favoritos = Favoritar.objects.filter(user=user)
    return render(request, 'favoritos/favoritos.html', {'favoritos': favoritos})

@login_required
def add_favoritos(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    if not Favoritar.objects.filter(user=user, product=product).exists():
        favoritar = Favoritar(user=user, product=product)
        favoritar.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remover_dos_favoritos(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    try:
        favorito = Favoritar.objects.get(user=user, product=product)
        favorito.delete()
    except Favoritar.DoesNotExist:
        pass 

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def pagamento(request):
    if request.method == "POST":
        metodo_pagamento = request.POST.get("metodo_pagamento")

        if metodo_pagamento == "pix":
            user = request.user
            pedido, created = Pedido.objects.get_or_create(user=user)

            pedido.codigo_pix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            pedido.status_pagamento = "pending"
            pedido.save()

            time.sleep(10)
            pedido.status_pagamento = "paid"
            pedido.save()
            return HttpResponse(f"Seu código PIX para pagamento: {pedido.codigo_pix}")

        elif metodo_pagamento == "cartao":
            pagamento_simulado = pagamento_com_cartao()
            if pagamento_simulado:
                pedido = Pedido.objects.create(user=request.user, status_pagamento="paid")

                return HttpResponse("Pagamento com cartão bem-sucedido. Pedido registrado.")
            return HttpResponse("Erro no pagamento com cartão. Verifique as informações do cartão.")

        
        elif metodo_pagamento == "pagar_retirada":
            user = request.user
            pedido, created = Pedido.objects.get_or_create(user=user)
            pedido.status_pagamento = "pending"
            pedido.save()
            return HttpResponse("Seu pedido foi registrado. O pagamento será efetuado na retirada.")
    
    return render(request, 'pagamento/pagamento.html')