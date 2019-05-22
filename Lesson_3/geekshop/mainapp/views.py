from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import BasketSlot




context = {'main': 'главная', 'contacts': 'контакты', '2070_gtx': 'видеокарта 2070 GTX',
          '2080_gtx': 'видеокарта 2080 GTX', }


def main(request):
    return render(request, 'mainapp/index.html')
    

def products(request, pk=None):
    if pk or pk == 0:
        product_objects = Product.objects.all()
        if pk:
            get_object_or_404(ProductCategory, pk=pk)
            product_objects = Product.objects.filter(category=pk)
        context = {'products': product_objects, 'productsCategory': ProductCategory.objects.all(),
                   'catalog': 'каталог товаров', }
        return render(request, 'mainapp/catalog.html', context)

    else:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {'hot_product': hot_product, 'productsCategory': ProductCategory.objects.all(),
                   'catalog': 'каталог товаров', }
        return render(request, 'mainapp/hot_product.html', context)
    

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


def get_basket(user):
    if user.is_authenticated:
        return BasketSlot.objects.filter(user=user)
    else:
        return []



def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)