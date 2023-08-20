# Generated by Django 3.2.12 on 2023-05-26 15:25

import Services.formatChecker
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=400, verbose_name='comments')),
                ('target', models.IntegerField(verbose_name='Review Target')),
                ('autor_raiting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_raiting', to='main.raiting')),
                ('product_raiting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_raiting', to='main.raiting')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(max_length=400, verbose_name='description')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1)], verbose_name='price')),
                ('isAvailable', models.BooleanField(default=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('owner', models.IntegerField(verbose_name='Product Owner')),
                ('fileEntity', Services.formatChecker.ContentTypeRestrictedFileField(upload_to='files/')),
                ('fileEntityHashSSH256', models.CharField(default='default_value', max_length=400, verbose_name='fileHash')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
