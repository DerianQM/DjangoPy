from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser


class IsSuperUserViev(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProductListViev(IsSuperUserViev,ListView):
    model = Product
    template_name = 'adminapp/products.html'


    def get_queryset(self):
        qs= super(ProductListViev, self).get_queryset()
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            return qs.filter(category__pk=category_pk)
        else:
            return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListViev, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Продукты'
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailViev(IsSuperUserViev,DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailViev, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Продукт'
        return context

class ProductUpdateViev(IsSuperUserViev,UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateViev, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Редактирование продукта'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk':self.kwargs.get('pk')})

class ProductCreateViev(IsSuperUserViev,CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:products')

class ProductDeleteViev(IsSuperUserViev,DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')


class ProductCategoryListView(IsSuperUserViev,ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context



class ProductCategoryCreateView(IsSuperUserViev,CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class ProductCategoryUpdateView(IsSuperUserViev,UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменение категории'
        return context


class ProductCategoryDeleteView(IsSuperUserViev,DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        return context


class ShopUserListView(IsSuperUserViev,ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        context = super(ShopUserListView, self).get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context




class ShopUserCreateView(IsSuperUserViev,CreateView):
    model = ShopUser
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(ShopUserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        return context


class ShopUserUpdateView(IsSuperUserViev,UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(ShopUserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменение пользователя'
        return context


class ShopUserDeleteView(IsSuperUserViev,DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(ShopUserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'пользователя'
        return context

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.success_url)