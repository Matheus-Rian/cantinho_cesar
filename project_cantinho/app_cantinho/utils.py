from .models import Pedido, Product, Cart

def total_pedido(pedido):
    produtos_no_pedido = pedido.products.all()

    total = 0

    for produto in produtos_no_pedido:
        total += produto.value  

    return total

def atualizar_estoque_produto(pedido):
    if pedido.status_pagamento == "paid":
        produtos_no_pedido = pedido.products.all()
        for produto in produtos_no_pedido:
            produto.stock -= 1 
            produto.save()
        carrinho = Cart.objects.get(user=pedido.user)
        carrinho.products.clear()
        carrinho.total = 0.00
        carrinho.hora_retirada = None
        carrinho.save()