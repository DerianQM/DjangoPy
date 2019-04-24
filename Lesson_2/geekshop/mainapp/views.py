from django.shortcuts import render

links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products', 'name': 'Каталог товаров'},
        {'href': 'contact', 'name': 'Контакты'}

]
context = {'main': 'главная', 'products': 'каталог товаров', 'contacts': 'контакты', '2070_gtx': 'видеокарта 2070 GTX',
           '2080_gtx': 'видеокарта 2080 GTX', '2080_ti': 'видеокарта 2080TI GTX','links_menu': links_menu}


def main(request):
    return render(request, 'mainapp/index.html', context)
    

def products(request):
    return render(request, 'mainapp/catalog.html', context)
    

def contact(request):
    return render(request, 'mainapp/contacts.html', context)


def page_2080ti(request):
    return render(request, 'mainapp/catalog/2080ti.html', context)


def page_2080(request):
    return render(request, 'mainapp/catalog/2080.html', context)


def page_2070(request):
    return render(request, 'mainapp/catalog/2070.html', context)