# Generated by Django 3.0.3 on 2020-03-29 17:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0011_auto_20200328_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img2',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img3',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img4',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img5',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
    ]
