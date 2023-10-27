from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("menu/", views.menu, name="menu"),
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
]
