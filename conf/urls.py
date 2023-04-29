from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

admin.site.site_title = admin.site.index_title\
    = admin.site.site_header = settings.WEBNAME

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True: urlpatterns += [
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
