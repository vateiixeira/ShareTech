from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('product', Product_List)
router.register('user', User_List, basename='user')
router.register('favorito', Favorito_List)
router.register('avatar', Avatar_List)
#router.register('img', Img_List.as_view())

urlpatterns = [
    path('csrf', Get_Csrf.as_view()),
    path('', include(router.urls)),
    path('img', Img_List.as_view()),
    path('get_user_name/<str:email>', User_List.as_view({'get':'getByUsername'})),
    path('loja/<int:id>', Product_List.as_view({'get':'dono'})),
    path('register', create_auth),
    path('favoritos/<int:pk>', FavoritoDetail.as_view()),
    path('change_avatar/user/<int:id>', Avatar_List.as_view({'put':'putbyId'})),
]
