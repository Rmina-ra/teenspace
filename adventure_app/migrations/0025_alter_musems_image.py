# Generated by Django 5.1.2 on 2024-10-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0024_alter_musems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musems',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
