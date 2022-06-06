# Generated by Django 4.0.4 on 2022-06-05 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipogenero', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'genero',
                'verbose_name_plural': 'generos',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('duracionminutos', models.IntegerField()),
                ('actores', models.CharField(max_length=100)),
                ('creacion', models.DateField()),
                ('SKU', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'pelicula',
                'verbose_name_plural': 'peliculas',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinopsis', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'resumen',
                'verbose_name_plural': 'resumen',
            },
        ),
    ]