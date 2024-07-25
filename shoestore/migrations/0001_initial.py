# Generated by Django 5.0.7 on 2024-07-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Female', max_length=6)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Female', max_length=6)),
                ('size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='')),
                ('isActive', models.BooleanField(default=True)),
                ('isHome', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('categories', models.ManyToManyField(to='shoestore.category')),
            ],
        ),
    ]
