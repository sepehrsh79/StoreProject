from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from eshop_products.models import Product

class Tag (models.Model):
    title = models.CharField(max_length=120,verbose_name='عنوان')
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now=True,verbose_name='عنوان در url')
    active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ '
        verbose_name_plural = 'تگ ها'

def tag_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =unique_slug_generator(instance)

pre_save.connect(tag_pre_save_reciever, sender=Tag)
