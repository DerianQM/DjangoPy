from django.urls import path

from .views import add, delete ,basket , edit, remove

app_name = 'basketapp'

urlpatterns = [
   path('', basket, name='edit'),
   path('add/product/<int:pk>/', add, name='add'),
   path('delete/product/<int:pk>/', delete, name='delete'),
   path('edit/<int:pk>/', edit, name='edit'),
   path('remove/product/<int:pk>/', remove, name='remove'),
]