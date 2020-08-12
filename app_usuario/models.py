# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class CpfUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        cpf = kwargs["cpf"]
        password = kwargs["password"]
        kwargs.pop("password")

        if not cpf:
            raise ValueError(_('Usuarios tem que fornecer cpf.'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Endereco de email'), blank=True, null=True,
    )
    phone = models.CharField(max_length=14, verbose_name=_(u'Telefone para contato'), null=True, blank=True)
    whatsapp = models.CharField(max_length=14, verbose_name=_(u'whatsapp para contato'), null=True, blank=True)
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=250,
        blank=False,
        help_text=_('Informe seu primeiro nome'),
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=250,
        blank=False,
        help_text=_('Informe seu sobrenome'),
    )
    birtday = models.DateField(verbose_name=_('Data de Nascimento'), null=False, blank=False)
    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=14,
        blank=False,
        unique=True,
        help_text=_('Informe seu CPF'),
    )

    street = models.CharField(max_length=250, verbose_name=_('Rua'), help_text=_('Informe seu nome da sua rua'), null=True, blank=True)
    neighborhood = models.CharField(max_length=250, verbose_name=_('Bairro'), help_text=_('Informe seu nome do seu bairro'), null=True, blank=True )
    city = models.CharField(max_length=250, verbose_name=_('Cidade'), help_text=_('Informe sua cidade'), null=True, blank=True )

    def __str__(self):
        return self.cpf

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'cpf'
    objects = CpfUserManager()

    class Meta:
        verbose_name_plural = 'Usuarios do sistema Varejista'
