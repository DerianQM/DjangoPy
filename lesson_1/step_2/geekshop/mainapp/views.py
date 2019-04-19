from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')
    

def products(request):
    return render(request, 'mainapp/catalog.html')
    

def contact(request):
    return render(request, 'mainapp/contacts.html')


def page_2080ti(request):
    return render(request, 'mainapp/catalog/2080ti.html')


def page_2080(request):
    return render(request, 'mainapp/catalog/2080.html')


def page_2070(request):
    return render(request, 'mainapp/catalog/2070.html')