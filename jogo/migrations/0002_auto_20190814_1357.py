# Generated by Django 2.2.2 on 2019-08-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adversario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('escudo_adversario', models.ImageField(blank=True, default='/adversarios/sem_escudo.png', null=True, upload_to='adversarios')),
                ('telefone', models.CharField(default='', max_length=14)),
            ],
            options={
                'verbose_name': 'Adversário',
                'verbose_name_plural': 'Adversários',
                'db_table': 'adversario',
            },
        ),
        migrations.CreateModel(
            name='Conquista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.PositiveIntegerField(default=0)),
                ('tipo', models.CharField(choices=[('1', 'Gols'), ('2', 'Assitencias'), ('3', 'Jogos'), ('4', 'Defesas'), ('5', 'Hat-Trick')], max_length=2)),
                ('imagem', models.ImageField(blank=True, default='/adversarios/sem_escudo.png', null=True, upload_to='adversarios')),
            ],
            options={
                'verbose_name': 'Conquista',
                'verbose_name_plural': 'Conquistas',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='galeria')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria',
                'db_table': 'galeria',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
                'db_table': 'local',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('corpo', models.TextField()),
                ('data_inclusao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'db_table': 'noticia',
            },
        ),
        migrations.AlterModelOptions(
            name='jogo',
            options={'ordering': ('-data',), 'verbose_name': 'Jogo', 'verbose_name_plural': 'Jogos'},
        ),
        migrations.AlterModelOptions(
            name='jogoatleta',
            options={'verbose_name': 'JogoAtleta', 'verbose_name_plural': 'JogoAtletas'},
        ),
        migrations.RemoveField(
            model_name='atleta',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='jogo',
            name='arbitragem',
        ),
        migrations.RemoveField(
            model_name='jogo',
            name='escudo_adversario',
        ),
        migrations.AddField(
            model_name='atleta',
            name='numero_camisa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atleta',
            name='status_jogador',
            field=models.CharField(choices=[('1', 'Elenco Principal'), ('2', 'Departamento Médico'), ('3', 'Aposentado'), ('4', 'Convidado'), ('5', 'Suspenso')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='jogoatleta',
            name='asssitencia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jogoatleta',
            name='defesas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jogoatleta',
            name='gols',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jogoatleta',
            name='minutos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jogoatleta',
            name='roubo_de_bola',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='imagem',
            field=models.ImageField(blank=True, default='/adversarios/sem-foto.png', null=True, upload_to='adversarios'),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='adversario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jogo.Adversario'),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jogo.Local'),
        ),
        migrations.AlterField(
            model_name='jogoatleta',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogadores', to='jogo.Jogo'),
        ),
        migrations.AlterModelTable(
            name='jogoatleta',
            table='jogo_x_atleta',
        ),
        migrations.CreateModel(
            name='ConquistaAtleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_conquista', models.DateField(auto_now_add=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conquistas', to='jogo.Atleta')),
                ('conquista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jogo.Conquista')),
            ],
        ),
    ]
