from rest_framework import serializers
from sharetech.produto.models import Produto, Img, Favorito
from sharetech.account.models import User, Avatar


class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(Product_Serializer, self).to_representation(instance)
        if instance.img1 is not None:
            representation['img1'] = instance.img1.url
        if instance.img2 is not None:
            representation['img2'] = instance.img2.url
        if instance.img3 is not None:
            representation['img3'] = instance.img3.url
        if instance.img4 is not None:
             representation['img4'] = instance.img4.url
        return representation

class Favorito_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class Img_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'rua', 'bairro', 'cep', 'fone', 'num_rua', 'email', 'cidade']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']

class AvatarSerializzer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'