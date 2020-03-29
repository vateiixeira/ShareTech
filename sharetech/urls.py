from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('sharetech.account.urls')),
    path('produto/', include('sharetech.produto.urls')),
    path('', include('sharetech.core.urls')),
    path('api/', include('sharetech.api.urls')),    
    path('rest-auth/', include('rest_auth.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
