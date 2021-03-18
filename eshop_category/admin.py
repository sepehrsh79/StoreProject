from django.contrib import admin
from .models import ProductsCaregory

@admin.register(ProductsCaregory)
class CategoryAdmin (admin.ModelAdmin):

    list_display = ['__str__', 'name']

    class Meta:

        model = ProductsCaregory