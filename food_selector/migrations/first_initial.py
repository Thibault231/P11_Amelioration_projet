# Generated by Django 3.0.5 on 2020-05-06 13:51
"""Migration for DB of Nutella_project on
Postgre SQL.
"""
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Class Migration for migration
    on DB.
    """
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID')),
                (
                    'name',
                    models.CharField(
                        max_length=100,
                        unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False, verbose_name='ID')),
                (
                    'name',
                    models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('allergens', models.TextField(default=None)),
                ('nutriscore', models.CharField(max_length=1)),
                ('store', models.CharField(max_length=100)),
                ('picture', models.URLField()),
                ('url_OpenFF', models.URLField()),
                ('linked_cat',
                 models.ManyToManyField(to='food_selector.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('history',
                 models.ManyToManyField(to='food_selector.FoodItem')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
