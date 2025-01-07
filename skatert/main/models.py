from django.db import models

class Category(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tablecloth(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='oilcloths')
    image1= models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клеёнка'
        verbose_name_plural = 'Клеёнки'



