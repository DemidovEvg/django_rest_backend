
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import mixins
from userapp.serializers import UserSerializer, UserSerializerV2
from rest_framework.viewsets import GenericViewSet


User = get_user_model()


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()

    # serializer_class = UserSerializer

    def get_serializer_class(self):
        if not self.request or not self.request.version or self.request.version == '1':
            return UserSerializer
        elif self.request.version == '2':
            return UserSerializerV2
        raise Http404
