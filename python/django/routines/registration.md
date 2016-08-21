# Registration for .json and .api


Abhängigkeiten installieren

```sh
pip install django-registration-redux
```

```python
# settings.py
INSTALLED_APPS += (
    'registration',
)
```



Registration urls verknüpfen
Beispiel root in url conf

```python
url(r'^accounts/', include('registration.backends.default.urls')),
```

Templates aus Lib Order in geeignete App kopieren
lib/pythonX.Y/site-packages/registration/templates -> whatever


URls Verknüpfen

```python
url(r'^', include('project.apps.appname.urls')),
```

Beispiel Config
```python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^accounts/auth/token/(?P<token>[a-f0-9]+)/$', views.TokenDetailView.as_view()),
]
```

Beispiel views.py

```python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache
from rest_framework import parsers, renderers, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class RegistrationView(APIView):

    serializer_class = serializers.UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response()

    def post(self, request):
        serializer = serializers.UserRegisterSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer._errors, status=400)


class LoginView(APIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        request.data['username'] = request.data.get('username', '').lower()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class TokenDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    @never_cache
    def get(self, request, token):
        token = get_object_or_404(Token, pk=token)
        serializer = serializers.TokenSerializer(token, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, token):
        token = get_object_or_404(Token, pk=token)
        token.delete()
        return Response(True)
```
