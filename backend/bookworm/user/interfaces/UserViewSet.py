from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from bookworm.user.interfaces.serializers import UserSerializer
from bookworm.user.models import AppUser


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AppUser.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = AppUser.objects.get(uuid=lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
