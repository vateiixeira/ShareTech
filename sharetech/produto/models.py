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
    marca_modelo = models.CharField('Marca', max_length=100, null=True, blank=True)
    preco = models.FloatField('Preco')
    descricao = models.TextField('Descricao')
    aceita_cartao = models.BooleanField('Aceita cartao' , default=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    img1 =  CloudinaryField('imagem', null=True)
    img2 =  CloudinaryField('imagem', null=True)
    img3 =  CloudinaryField('imagem', null=True)
    img4 =  CloudinaryField('imagem', null=True)

    create_at = models.DateField('Criado em')
    updated_at = models.DateField('Atualizado em')

    # True == Aceita cartao

    def __str__(self):
        return str(f" Categoria:{self.nome} | Modelo:{self.modelo}")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['modelo']

    objects = UserManager()

class Img(models.Model):
    img =  models.ImageField(upload_to='images/')  

    objects = UserManager()

class Favorito (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    objects = UserManager()



    