from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField('Название места',max_length=150)
    description_short = models.TextField('Краткое описание',blank=True)
    description_long = HTMLField('Длинное описание',blank=True)
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'



class PlaceImage(models.Model):
    place = models.ForeignKey(
                                Place, on_delete=models.CASCADE,
                                verbose_name='Место',
                                related_name='place_images')
    image = models.ImageField('Изображение')
    position = models.PositiveIntegerField('Позиция',default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображениe'
        verbose_name_plural = 'Изображения'






