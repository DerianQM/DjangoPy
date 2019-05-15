from django.urls import path

from .views import add,delete

app_name = 'basketapp'

urlpatterns = [
   path('add/product/<int:pk>/', add, name='add'),
   path('delete/product/<int:pk>/', delete, name='delete'),
]