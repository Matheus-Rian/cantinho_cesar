from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
  name = models.CharField(max_length=200)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  link = models.URLField()
  stock = models.IntegerField(default=0)
  disponivel = models.BooleanField(default=True)
  def __str__(self):
    return self.name

class Vendinha(models.Model):
  name = models.CharField(max_length=200)
  products = models.ManyToManyField(Product)


class Cart(models.Model):
  name = models.CharField(max_length=200, default='Carrinho')
  products = models.ManyToManyField(Product)
  total = models.DecimalField(max_digits=100, decimal_places=2)

class VendinhaController():
  def get_vendinha_by_name(name):
    return Vendinha.objects.get(name=name)

class CartController():
  def add_to_cart(product):
    cart = Cart.objects.get(name='Carrinho')
    cart.products.add(product)
  def get_cart_by_name(name):
    return Cart.objects.get(name='Carrinho')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products_cart = models.ManyToManyField(Product)
    def __str__(self):
        return self.user.username
    