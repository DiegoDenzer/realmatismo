# Generated by Django 2.2.2 on 2019-09-16 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0002_auto_20190814_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('data_inclusao', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('data_vencimento', models.DateTimeField()),
                ('data_pagamento', models.DateTimeField(null=True)),
                ('tipo_fatura', models.CharField(choices=[('R', 'RECEITA'), ('D', 'DESPESA')], max_length=2)),
                ('valor_fatura', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('valor_pago', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('1', 'Elenco Principal'), ('2', 'Departamento Médico'), ('3', 'Aposentado'), ('4', 'Convidado'), ('5', 'Suspenso')], max_length=1, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('1', 'Mensalidade'), ('2', 'Viagem'), ('3', 'Material Esportivo'), ('4', 'Churrasco'), ('5', 'Outros')], max_length=2, null=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jogo.Atleta')),
            ],
        ),
    ]
