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

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    vendinha = models.ForeignKey(Vendinha, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return f"Review for {self.product.name} at {self.vendinha.name} by {self.user.username}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    products = models.ManyToManyField(Product, blank = True)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
    def __str__(self):
        return str(self.id)
    
class Pedido(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True, blank = True)  
  products = models.ManyToManyField(Product, blank = True)
  total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
  hora_retirada = models.TimeField(null=True, blank=True)
  status_pagamento = models.CharField(max_length=20, default="pending")
  codigo_pix = models.CharField(max_length=20, blank=True, null=True)
  def __str__(self):
      return str(self.id)
  @classmethod
  def create_with_default_cart(cls, user):
      cart, _ = Cart.objects.get_or_create(user=user)
      return cls.objects.create(user=user, cart=cart)
    
    
class VendinhaController():
  def get_vendinha_by_name(name):
    return Vendinha.objects.get(name=name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    def __str__(self):
        return self.user.username
  
class Favoritar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    


