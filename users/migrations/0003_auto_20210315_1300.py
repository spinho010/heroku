# Generated by Django 3.1.7 on 2021-03-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(default='/static/midia/10.png', upload_to='D:/', verbose_name='Foto'),
        ),
    ]
