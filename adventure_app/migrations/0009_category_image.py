# Generated by Django 5.1.2 on 2024-10-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0008_alter_kino_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default='укажите изображение', max_length=500, verbose_name='URL-фото'),
        ),
    ]
