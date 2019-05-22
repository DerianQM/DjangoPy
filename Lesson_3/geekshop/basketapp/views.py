from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import BasketSlot
from mainapp.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    return render(request, 'basketapp/basket.html', {'basket_items': basket})





@login_required
def add(request, pk=None):

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main'))
    else:
        product = get_object_or_404(Product, pk=pk)
        basket_slot_old = BasketSlot.objects.filter(product=product).first()
        if basket_slot_old:
            basket_slot_old.quantity += 1
            basket_slot_old.save()
        else:
            basket_slot = BasketSlot(product=product, user=request.user)
            basket_slot.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(product=product).first()

    if basket_slot:
        if  basket_slot.quantity > 1:
            basket_slot.quantity -=1
            basket_slot.save()
        else:
            basket_slot.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def edit(request, pk=None):
    if request.is_ajax():
        basket_slot = get_object_or_404(BasketSlot, pk=pk)
        if request.GET.get('quantity'):
            basket_slot.quantity = request.GET.get('quantity')
            basket_slot.save()
        return HttpResponse('OK')


@login_required
def remove(request, pk=None):
    basket_record = get_object_or_404(BasketSlot, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


