from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_title = admin.site.site_header\
    = admin.site.index_title = settings.WEBNAME

if settings.DEBUG == True: urlpatterns += [
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
