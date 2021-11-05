# Generated by Django 3.1.7 on 2021-11-04 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_estatuto'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DispoI', models.CharField(blank=True, max_length=60, null=True, verbose_name='Disponibilidade do item:')),
                ('obsII', models.CharField(blank=True, max_length=60, null=True, verbose_name='Obs Item: ')),
            ],
        ),
        migrations.CreateModel(
            name='statusItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatusI', models.CharField(blank=True, max_length=60, null=True, verbose_name='Status do item:')),
                ('obsI', models.CharField(blank=True, max_length=60, null=True, verbose_name='Obs Item: ')),
            ],
        ),
        migrations.CreateModel(
            name='patrimonioibb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome: ')),
                ('quantidade_item', models.IntegerField(blank=True, null=True, verbose_name='Quantidade: ')),
                ('obs_item', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observações: ')),
                ('doador_item', models.CharField(blank=True, max_length=100, null=True, verbose_name='Doado por: ')),
                ('dispon_item', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.dispoitem')),
                ('status_item', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.statusitem')),
            ],
        ),
    ]