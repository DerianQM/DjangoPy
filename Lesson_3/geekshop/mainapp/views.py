from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import BasketSlot




context = {'main': 'главная', 'contacts': 'контакты', '2070_gtx': 'видеокарта 2070 GTX',
           '2080_gtx': 'видеокарта 2080 GTX', }


def main(request):
    return render(request, 'mainapp/index.html')
    

def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = BasketSlot.objects.filter(user=request.user)
    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
    if pk:
        get_object_or_404(ProductCategory, pk=pk)
        context = {'products': Product.objects.filter(category=pk), 'productsCategory': ProductCategory.objects.all(),
                   'catalog': 'каталог товаров','basket_quantity': total_quantity}
    else:
        context = {'products': Product.objects.all(), 'productsCategory': ProductCategory.objects.all(),
                   'catalog': 'каталог товаров', 'basket_quantity': total_quantity}

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