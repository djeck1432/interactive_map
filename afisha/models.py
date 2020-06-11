from django.db import models
from django.contrib import admin
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField('Название места',max_length=150)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Длинное описание')
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

def get_image_position():
    extra = admin.TabularInline.extra
    print(extra)

class PlaceImage(models.Model):
    place = models.ForeignKey(
                                Place, on_delete=models.CASCADE,
                                verbose_name='Место',
                                related_name='place_images')
    image = models.ImageField('Изображение', blank=True)
    position = models.PositiveIntegerField('Позиция',default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображениe'
        verbose_name_plural = 'Изображения'






