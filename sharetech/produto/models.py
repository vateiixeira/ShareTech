from django.db import models
from django.contrib.auth.models import UserManager
from sharetech.account.models import User
from cloudinary.models import CloudinaryField

# CATEGORIA_PRODUTO = (
#     ('GABINETE','GABINETE' ),
#     ('PROCESSADOR','PROCESSADOR' ),
#     ('PLACA-MAE','PLACA-MAE' ),
#     ('MEMORIA','MEMORIA' ),
#     ('HD','HD' ),
#     ('SSD','SSD' ),
#     ('COOLER','COOLER' ),
#     ('FONTE','FONTE' ),
#     ('DISPLAY','DISPLAY' ),
#     ('OUTROS','OUTROS' ),
# )


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    marca_modelo = models.CharField('Modelo ou Marca', max_length=100, null=True, blank=True)
    preco = models.FloatField('Preco')
    descricao = models.TextField('Descricao')
    aceita_cartao = models.BooleanField('Aceita cartao' , default=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    img1 =  models.CharField('img1', max_length=400, null=True)
    img2 =  models.CharField('img2', max_length=400, null=True)
    img3 =  models.CharField('img3', max_length=400, null=True)
    img4 =  models.CharField('img4', max_length=400, null=True)

    create_at = models.DateField('Criado em')
    updated_at = models.DateField('Atualizado em')

    # True == Aceita cartao

    def __str__(self):
        return str(f" Categoria:{self.nome} | Modelo:{self.marca_modelo}")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['marca_modelo']

    objects = UserManager()

class Img(models.Model):
    img =  models.ImageField(upload_to='images/')  

    objects = UserManager()

class Favorito (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    objects = UserManager()



    