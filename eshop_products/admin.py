from django.contrib import admin
from .models import Product,ProductGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'active']

    class Meta:
        model = Product


admin.site.register(ProductGallery)
