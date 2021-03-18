from django.shortcuts import render, get_object_or_404, redirect
import itertools

from eshop_products.models import Product
from eshop_slider.models import Slider
from eshop_setting.models import SiteSetting

#header code behind
def header (request ,*args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)

#Footer code behind
def footer (request ,*args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
    'setting' : site_setting
    }
    return render(request, 'shared/Footer.html', context)


def my_grouper (n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None]for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    most_view_product = Product.objects.order_by('-visit_count').all()[:8]
    latest_product = Product.objects.order_by('-id').all()[:8]
    context = {
        "data" : "newdata",
        "sliders": sliders,
        "most_view": my_grouper(4,most_view_product),
        "lates_products" : my_grouper(4, latest_product)
    }
    return render(request,"home_page.html",context)


def about_page (request):
    site_setting = SiteSetting.objects.first()
    context = {
    'setting' : site_setting
    }
    return render(request, 'about_page.html', context)
