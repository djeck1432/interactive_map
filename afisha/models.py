from django.db import models

class Places(models.Model):
    title = models.CharField('Названия места',max_length=150)

    description_short = models.CharField('Краткое описания', max_length=300)
    description_long = models.TextField('Полное описания')
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

class PlaceImages(models.Model):
    place = models.ForeignKey(
                                Places, on_delete=models.CASCADE,
                                verbose_name='Место',
                                related_name='image')
    images = models.ImageField('Изображения')




