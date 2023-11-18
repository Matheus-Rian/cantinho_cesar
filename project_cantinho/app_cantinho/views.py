from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import OptionsVendinha
from .models import VendinhaController, Product, Cart,UserProfile,Favoritar, Pedido
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import total_pedido, atualizar_estoque_produto
from decimal import Decimal
import random, string
from django.contrib import messages

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
    carrinho.total = total
    carrinho.save()
    
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


    if usuario_aux.email=="vendedor@gmail.com" and usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/vendedor/')    
    elif usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/menu/')
    else:
        messages.error(request, "Credenciais incorretas")
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

        pedidos_em_andamento = Pedido.objects.filter(user=user, status_pagamento__in=["pending"])


        if not pedidos_em_andamento.exists():
            pedido = Pedido.objects.create(user=user, status_pagamento="pending", hora_retirada=hora_retirada)
            messages.success(request, "Novo pedido criado com horário.")
        else:
            messages.warning(request, "Já existe um pedido em andamento ou pago. Você não pode criar um novo.")

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
    context = {}
    if request.method == "POST":
        metodo_pagamento = request.POST.get("metodo_pagamento")

        if metodo_pagamento == "pix":
            
            user = request.user
            carrinho = Cart.objects.get(user=user)
            pedido = Pedido.objects.filter(user=user, status_pagamento="pending").first()

            if pedido:
                pedido.cart = carrinho
                pedido.products.set(carrinho.products.all())
                total = total_pedido(pedido)
                pedido.total = total
                pedido.codigo_pix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                pedido.status_pagamento = "paid"
                pedido.save()

                atualizar_estoque_produto(pedido)

                carrinho.products.clear()
                carrinho.total = 0.00
                carrinho.save()
                return render(request, 'codigo/codigo.html', {'codigo_pix': pedido.codigo_pix})

        
        elif metodo_pagamento == "pagar_retirada":
            user = request.user
            pedido = Pedido.objects.filter(user=user, status_pagamento="pending").first()
            carrinho = Cart.objects.get(user=user)
            if pedido:
                pedido.cart = carrinho
                pedido.products.set(carrinho.products.all())
                total = total_pedido(pedido)
                pedido.total = total
                pedido.status_pagamento = "pending"
                pedido.save()
                return render(request, 'retirada/retirada.html')

        elif metodo_pagamento == "saldo":
            user = request.user
            carrinho = Cart.objects.get(user=user)
            pedido = Pedido.objects.filter(user=user, status_pagamento="pending").first()

            if pedido:
                pedido.cart = carrinho
                pedido.products.set(carrinho.products.all())
                total = total_pedido(pedido)
                pedido.total = total
                pedido.save()

                if user.userprofile.saldo >= pedido.total:
                   
                    user.userprofile.saldo -= pedido.total
                    user.userprofile.save()

                    pedido.status_pagamento = "paid"
                    pedido.save()

                    messages.success(request,'Pagamento realizado com sucesso!')
                    return redirect('resumo_compra')
                else:
                    messages.error(request, 'Saldo insuficiente para realizar o pagamento com saldo.')
                    # Adiciona uma mensagem de erro e redireciona para a página de pagamento
                    return redirect('pagamento')
    return render(request, 'pagamento/pagamento.html')




def resumo_compra(request):
    user = request.user
    carrinho = Cart.objects.get(user=user)
    produtos = carrinho.products.all()
    total = sum(produto.value for produto in produtos)


    pedido = Pedido.objects.filter(user=user).order_by('-id').first()

    if pedido:
        status_pagamento = pedido.status_pagamento
    else:
        status_pagamento = "Não encontrado" 

    context = {
        'produtos': produtos,
        'total': total,
        'hora_retirada': pedido.hora_retirada,
        'status_pagamento': status_pagamento,
    }

    return render(request, 'resumo_compra/resumo_compra.html', context)

@login_required
def remover_carrinho(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    
    try:
        carrinho = Cart.objects.get(user=user)        
        carrinho.products.remove(product)
    except Cart.DoesNotExist:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def adicionar_saldo(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        valor_adicional = Decimal(request.POST.get('valor_adicional', 0.0))

        if valor_adicional > 0:
            user_profile.saldo += valor_adicional
            user_profile.save()

            messages.success(request, f'Saldo de R${valor_adicional:.2f} adicionado com sucesso!')

        else:
            messages.error(request, 'O valor a ser adicionado deve ser maior que zero.')

    return render(request, 'adicionar_saldo/adicionar_saldo.html', {'user_profile': user_profile})

@login_required
def vendedor(request):
    pedidos = Pedido.objects.all()
    context = {
        'pedidos': pedidos,
    }
    return render(request, 'vendedor/vendedor.html', context)