from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()  
 

class Vendinha(models.Model):
  name = models.CharField(max_length=200)
  products = models.ManyToManyField(Product)

class User(models.Model):
  name = models.CharField(max_length=200)
  products_cart = models.ManyToManyField(Product)

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  products = models.ManyToManyField(Product, through='CartItem')
  created_at = models.DateTimeField()
  total = models.DecimalField(max_digits=100, decimal_places=2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class VendinhaController():
  def get_vendinha_by_name(name):
    return Vendinha.objects.get(name=name)

class CartController():
  def add_to_cart(vendinha, product_id, user):
    vendinha = Vendinha.objects.get(name=vendinha)
    product = vendinha.products.filter(product_id)
    cart = Cart.objects.get_or_create(user=user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
      cart_item.quantity += 1
      cart_item.save()
    
    return True



