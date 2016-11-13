# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url  # add include?
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # url(r'', include('apps.APPNAME.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
