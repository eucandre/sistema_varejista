from django.db import models

UN = (('kg','kg'),('l','l'),('peca','peca'),('duzia','duzia'),('par','par'))


class Category(models.Model):
    '''
    Esta classe busca categorisar os produtos para suas linhas de aplicação.
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categorias dos produtos'

class Product(models.Model):
    '''
    Classe que registra os produtos, estes possuem descrição, categorias(pode ser mais de uma), a marca(fabricante),
     o preço da unidade(diferente de cata tipo de produto) e data de validade.
    As variáveis categories, expiration_date e manufacturer serão manipuladas para promoções de desconto dos produtos.
    '''
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    #categories = models.ManyToManyField(Category)
    manufacturer = models.CharField(max_length=255)
    price = models.FloatField()
    unity = models.CharField(max_length=15, choices=UN)
    expiration_date = models.DateField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Produtos cadastrados no sitema de Varejo'

