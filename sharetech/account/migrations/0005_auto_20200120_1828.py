# Generated by Django 2.2.7 on 2020-01-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_usermore_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermore',
            name='cep',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermore',
            name='fone',
            field=models.CharField(max_length=20),
        ),
    ]
