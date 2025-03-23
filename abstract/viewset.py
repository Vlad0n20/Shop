from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny


from abstract.mixins import MixedPermission


class CustomModelViewSet(MixedPermission, ModelViewSet):
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }

