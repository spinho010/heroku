# Generated by Django 3.1.7 on 2021-03-24 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iuser',
            name='usuario',
        ),
    ]
