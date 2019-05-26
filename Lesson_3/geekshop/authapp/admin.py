from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot


admin.site.register(ShopUser)

class BasketInline(admin.TabularInline):
    model = BasketSlot
    fields = 'product', 'quantity',
    extra = 1





class UserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователь с корзиной'
        proxy = True

@admin.register(UserWithBasket)
class UserWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost'
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInline,

    def get_queryset(self, request):
        qs = super(UserWithBasketAdmin,self).get_queryset(request)
        return qs.filter(basket__quantity__gt=0).distinct()

    def get_basket_quantity(self,instance):
        basket= BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot:basket_slot.quantity,basket)))
    get_basket_quantity.short_description = 'Количество товаров в корзине'

    def get_basket_cost(self,instance):
        basket= BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda x: x.product.price * x.quantity,basket)))

    get_basket_cost.short_description = 'сумма товаров в корзине'