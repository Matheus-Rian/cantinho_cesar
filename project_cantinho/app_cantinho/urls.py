from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('add_to_cart/<int:product_id>/', views.Cart.as_view(), name='add_to_cart'),
  path("cadastrar/", views.pagina_de_cadastro, name='cadastrar'), 
  path("cadastrar_usuario/", views.cadastrar_usuario, name='cadastrar_usuario'),
]
