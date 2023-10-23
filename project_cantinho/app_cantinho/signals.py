from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def update_product_availability(sender, instance, **kwargs):
    if instance.stock <= 0 and instance.disponivel:
        instance.disponivel = False
        instance.save()
    elif instance.stock > 0 and not instance.disponivel:
        instance.disponivel = True
        instance.save()
