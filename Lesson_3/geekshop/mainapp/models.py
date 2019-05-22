from django.db import models

class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(verbose_name='имя категории',max_length=255,unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория товара')
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_hot = models.BooleanField(verbose_name='горячее предложение', default=False)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
