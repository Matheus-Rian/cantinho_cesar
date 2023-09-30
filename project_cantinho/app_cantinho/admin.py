from django.contrib import admin
from .models import Product, Vendinha, User, Cart

admin.site.register(Product)
admin.site.register(Vendinha)
admin.site.register(User)
admin.site.register(Cart)