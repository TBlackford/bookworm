from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from ts_generator.Route import route

from bookworm.auth.data.serializers import RegisterSerializer


@route('auth/register', name='Register', method=['post'])
class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    class Meta:
        request_data = ['username', 'email', 'password']

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh_token': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({
            'user': serializer.data,
            'refresh': res['refresh_token'],
            'access': res['access']
        }, status=status.HTTP_201_CREATED)
