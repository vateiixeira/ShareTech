# Generated by Django 2.2.7 on 2020-01-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_usermore_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermore',
            name='cep',
            field=models.IntegerField(null=True),
        ),
    ]
