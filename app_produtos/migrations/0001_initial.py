# Generated by Django 3.0.5 on 2020-08-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categorias dos produtos',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('unity', models.CharField(choices=[('kg', 'kg'), ('l', 'l'), ('peca', 'peca'), ('duzia', 'duzia'), ('par', 'par')], max_length=15)),
                ('expiration_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Produtos cadastrados no sitema de Varejo',
            },
        ),
    ]
