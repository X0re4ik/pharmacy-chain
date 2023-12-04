
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

VERSION_API = 1

api_url_patterns = [
    path('products/', include('product.urls')),
    path('', include('price.urls')),
    path('', include('pharmacy.urls')),
]

urlpatterns = [
    path(f'api/v{VERSION_API}/', include(api_url_patterns)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
