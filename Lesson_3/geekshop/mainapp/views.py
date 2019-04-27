from django.shortcuts import render
from .models import ProductCategory, Product





context = {'main': 'главная', 'contacts': 'контакты', '2070_gtx': 'видеокарта 2070 GTX',
           '2080_gtx': 'видеокарта 2080 GTX', }


def main(request):
    return render(request, 'mainapp/index.html', context)
    

def products(request, pk=None):
    if pk==None:
        context = {'products': Product.objects.all(),'productsCategory': ProductCategory.objects.all(),'catalog': 'каталог товаров'}
    else:
        context = {'products': Product.objects.filter(category=pk), 'productsCategory': ProductCategory.objects.all(),
                   'catalog': 'каталог товаров'}
    return render(request, 'mainapp/catalog.html', context)
    

def contact(request):
    return render(request, 'mainapp/contacts.html', context)


def page_2080ti(request):
    context = {'products': Product.objects.all(), 'productsCategory': ProductCategory.objects.all(),
               '2080_ti': 'видеокарта 2080TI GTX'}
    return render(request, 'mainapp/catalog/2080ti.html', context)


def page_2080(request):
    return render(request, 'mainapp/catalog/2080.html', context)


def page_2070(request):
    return render(request, 'mainapp/catalog/2070.html', context)