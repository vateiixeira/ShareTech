# Generated by Django 3.0.3 on 2020-03-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_usermore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bairro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='num_rua',
            field=models.IntegerField(null=True),
        ),
    ]
