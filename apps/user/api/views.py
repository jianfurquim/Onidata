from rest_framework import viewsets

from django.contrib.auth.models import User
from apps.user.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
