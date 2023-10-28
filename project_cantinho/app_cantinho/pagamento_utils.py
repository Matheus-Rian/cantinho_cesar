from .models import Pedido
from django.http import HttpResponse

def pagamento_com_cartao(numero_cartao, data_validade, codigo_cvc):

    resultado_pagamento = pagamento_com_cartao(numero_cartao, data_validade, codigo_cvc)

    if resultado_pagamento:
        pedido = Pedido.objects.create(user=request.user, status_pagamento="paid")
        return HttpResponse("Pagamento com cartão bem-sucedido. Pedido registrado.")
    else:
        return HttpResponse("Erro no pagamento com cartão. Verifique as informações do cartão.")
