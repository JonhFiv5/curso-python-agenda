# Generated by Django 3.1.4 on 2020-12-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m'),
        ),
    ]