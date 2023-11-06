from django.contrib import admin
from .models import Product, Vendinha, UserProfile, Cart,Favoritar, Pedido, Review

admin.site.register(Product)
admin.site.register(Pedido)
admin.site.register(Vendinha)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Favoritar)
admin.site.register(Review)