from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('add_to_cart/<int:product_id>/', views.Cart.as_view(), name='add_to_cart'),
]
