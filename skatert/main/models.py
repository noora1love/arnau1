from django.db import models
from PIL import Image

class Category(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    description_detail = models.TextField('Описание Детально', blank=True, null=True)
    size = models.TextField('Размер (N x N)', blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Сжимаем изображение категории, если оно задано
        if self.image:
            self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image_field):
        """
        Сжимаем изображение, уменьшая его качество до 70%.
        """
        try:
            img = Image.open(image_field)
            img.save(image_field.path, quality=70, optimize=True)
        except Exception as e:
            print(f"Ошибка при сжатии изображения категории: {e}")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tablecloth(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='oilcloths')
    image1 = models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='oilcloth_images/', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    number = models.CharField('Номер Клеенки', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Сжимаем изображения клеёнок, если они заданы
        if self.image1:
            self.compress_image(self.image1)
        if self.image2:
            self.compress_image(self.image2)
        if self.image3:
            self.compress_image(self.image3)
        super().save(*args, **kwargs)

    def compress_image(self, image_field):
        """
        Сжимаем изображение, уменьшая его качество до 70%.
        """
        try:
            img = Image.open(image_field)
            img.save(image_field.path, quality=70, optimize=True)
        except Exception as e:
            print(f"Ошибка при сжатии изображения клеёнки: {e}")

    class Meta:
        verbose_name = 'Клеёнка'
        verbose_name_plural = 'Клеёнки'
