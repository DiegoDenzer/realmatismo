# Generated by Django 2.2.2 on 2019-09-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0004_auto_20190916_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fatura',
            options={'ordering': ('-data_vencimento',), 'verbose_name': 'Fatura', 'verbose_name_plural': 'Faturas'},
        ),
    ]
