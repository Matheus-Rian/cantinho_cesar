from django.contrib import admin
from .models import Product, Vendinha, UserProfile, Cart

admin.site.register(Product)
admin.site.register(Vendinha)
admin.site.register(UserProfile)
admin.site.register(Cart)