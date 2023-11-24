from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("menu/", views.menu, name="menu"),
  path('avaliar_pedido/<int:produto_id>/<int:pedido_id>/', views.avaliar_pedido, name='avaliar_pedido'),
  path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
  path('carrinho/adicionar/<int:product_id>/', views.cart_home, name='carrinho'),
  path('carrinho/', views.carrinho, name='carrinho_sem_produto'),
  path("cadastrar/", views.pagina_de_cadastro, name='cadastrar'), 
  path("cadastrar_usuario/", views.cadastrar_usuario, name='cadastrar_usuario'),
  path("sair/", views.sair, name='sair'),
  path("entrar/", views.entrar, name='entrar'),
  path("salvar_horario", views.salvar_horario, name="salvar_horario"),
  path('meus-favoritos/', views.meus_favoritos, name='meus-favoritos'),
  path('adicionar-aos-favoritos/<int:product_id>/', views.add_favoritos, name='adicionar-aos-favoritos'),
  path('remover-dos-favoritos/<int:product_id>/', views.remover_dos_favoritos, name='remover-dos-favoritos'),
  path('pagamento/', views.pagamento, name='pagamento'),
  path('resumo_compra/', views.resumo_compra, name='resumo_compra'),
  path('remover_carrinho/<int:product_id>/', views.remover_carrinho, name='remover_carrinho'),
  path('adicionar_saldo/', views.adicionar_saldo, name='adicionar_saldo'),
  path('vendedor/', views.vendedor, name='vendedor'),

]
