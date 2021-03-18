import itertools
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from eshop_tag.models import Tag
from eshop_category.models import ProductsCaregory


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductsCaregory.objects.get(name__iexact=category_name)
        if category is None:
            raise Http404('صفحه مورد نظر پیدا نشد')
        return Product.objects.get_products_by_category(category_name)


def my_grouper (n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None]for t in itertools.zip_longest(*args))


def product_detail (request,*args, **kwargs):

    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None,initial = {'product_id': selected_product_id} )

    product: Product = Product.objects.get_by_id(selected_product_id)

    if product is None or not product.active :
        raise Http404('محصول مورد نظر یافت نشد')

    product.visit_count += 1
    product.save()

    related_products = Product.objects.get_queryset().filter(categoris__product= product).distinct()
    grouped_related_product = my_grouper(3,related_products)

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)
    grouped_galleries = list(my_grouper(3,galleries))

    context = {
        'product': product,
        'galleries' : grouped_galleries,
        'related_product': grouped_related_product,
        'new_order_form' : new_order_form,
    }


    return render(request, 'products/product_detail.html',context)

class SearchProductView (ListView):

    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None :
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def products_categories_partial (request ,*args, **kwargs):
    categories = ProductsCaregory.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'products/products_categories_partial.html', context)
