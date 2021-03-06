# Generated by Django 3.0.7 on 2020-06-11 16:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название места')),
                ('description_short', models.TextField(verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(verbose_name='Длинное описание')),
                ('long', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', to='afisha.Place', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Изображениe',
                'verbose_name_plural': 'Изображения',
                'ordering': ['position'],
            },
        ),
    ]
