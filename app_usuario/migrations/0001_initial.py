# Generated by Django 3.0.5 on 2020-08-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Endereco de email')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefone para contato')),
                ('whatsapp', models.CharField(blank=True, max_length=14, null=True, verbose_name='whatsapp para contato')),
                ('first_name', models.CharField(help_text='Informe seu primeiro nome', max_length=250, verbose_name='Nome')),
                ('last_name', models.CharField(help_text='Informe seu sobrenome', max_length=250, verbose_name='Nome')),
                ('birtday', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(help_text='Informe seu CPF', max_length=14, unique=True, verbose_name='CPF')),
                ('street', models.CharField(blank=True, help_text='Informe seu nome da sua rua', max_length=250, null=True, verbose_name='Rua')),
                ('neighborhood', models.CharField(blank=True, help_text='Informe seu nome do seu bairro', max_length=250, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, help_text='Informe sua cidade', max_length=250, null=True, verbose_name='Cidade')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuarios do sistema Varejista',
            },
        ),
    ]
