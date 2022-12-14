# Generated by Django 4.0.3 on 2022-09-20 13:28

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColoradoShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.CharField(max_length=128, verbose_name='Publicação Colorado Show')),
                ('descricao', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descrição')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('imagem', models.ImageField(upload_to=main.models.ImagemColorado, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='Imagem (420x520)')),
            ],
            options={
                'verbose_name': 'Colorado Show',
                'verbose_name_plural': '6.0 - Colorado Show',
            },
        ),
    ]
