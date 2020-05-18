from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from sharetech.produto.models import Produto, Img, Favorito
from sharetech.account.models import User, Avatar
from .serializers import Product_Serializer, User_Serializer, Img_Serializer, Favorito_Serializer,RegistrationSerializer, AvatarSerializzer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics

class Get_Csrf(APIView):
    def get(self, request, format=None):
        token = get_token(request)
        return Response(token)

class Product_List(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = Product_Serializer

    def dono(self, request, id ):
        user = User.objects.get(id=id)
        produto = Produto.objects.filter(vendedor=id)
        serializer = Product_Serializer(produto, many=True)
        return Response(serializer.data)

class FiltrarProduto(APIView): 

    def get_object(self, nome1, nome2, nome3, nome4):        
        try:
            nome = Produto.objects.filter(nome__in = [nome1, nome2, nome3, nome4])
            marca_modelo = Produto.objects.filter(marca_modelo__in = [nome1, nome2, nome3, nome4])
            contem = Produto.objects.filter(nome = '9879987')
            contem_marcaModelo = Produto.objects.filter(nome = '9879987') 
            
            for i in [nome1, nome2, nome3, nome4]:
                obj = Produto.objects.filter(nome__contains = i)
                contem = obj | contem

            for x in [nome1, nome2, nome3,nome4]:
                obj = Produto.objects.filter(marca_modelo__contains = x)
                contem_marcaModelo = obj | contem_marcaModelo

            total = nome | marca_modelo | contem | contem_marcaModelo
            return total
        except total is None:
            raise Http404

    def get(self, request, nome1, nome2, nome3, nome4, format=None):
        user = self.get_object(nome1, nome2, nome3, nome4)
        serializer = Product_Serializer(user, many=True)
        return Response(serializer.data)  

class Avatar_List(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializzer
    lookup_field = 'user'
    
    def putbyId(self, request, id ):
        avatar = Avatar.objects.get(user=id)
        serializer = AvatarSerializzer(avatar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Favorito_List(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = Favorito_Serializer

class FavoritoDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Favorito.objects.filter(user_id=pk)
        except Favorito.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = Favorito_Serializer(user, many=True)
        return Response(serializer.data)


# class Img_List(viewsets.ModelViewSet):
#     queryset = Img.objects.all()
#     serializer_class = Img_Serializer

class User_List(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

    def getByUsername(self, request, email ):
        user = get_object_or_404(User, email=email)
        return Response(User_Serializer(user).data, status=status.HTTP_200_OK)

class Img_List(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = Img_Serializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_auth(request):
    serialized = RegistrationSerializer(data=request.data)
    if serialized.is_valid():        
        User.objects.create_user(
            email = serialized.data['email'],
            username = serialized.data['username'],
            password = serialized.data['password'],
            first_name = serialized.data['first_name']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def last_products(request):
    produto = Produto.objects.all().order_by('id')[:20][::-1]
    serializer = Product_Serializer(produto, many=True)
    return Response(serializer.data)
