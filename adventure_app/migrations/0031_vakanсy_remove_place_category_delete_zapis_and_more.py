# Generated by Django 5.1.2 on 2024-12-05 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure_app', '0030_rename_descriprion_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vakanсy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('author', models.CharField(max_length=255, verbose_name='Работодатель')),
                ('cost', models.CharField(max_length=150, verbose_name='Зарплата')),
                ('phone', models.CharField(max_length=17, verbose_name='Номер телефона')),
                ('course', models.URLField(max_length=500, verbose_name='Ссылка на курсы')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.RemoveField(
            model_name='place',
            name='category',
        ),
        migrations.DeleteModel(
            name='Zapis',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
