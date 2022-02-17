from rest_framework.routers import SimpleRouter

from bookworm.auth.interfaces.viewsets import RefreshViewSet, LogoutViewSet, RegistrationViewSet, LoginViewSet
from bookworm.user.interfaces import UserViewSet
from bookworm.books.interfaces.viewsets import AuthorViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register('auth/login', LoginViewSet, basename='auth-login')
routes.register('auth/logout', LogoutViewSet, basename='auth-logout')
routes.register('auth/register', RegistrationViewSet, basename='auth-register')
routes.register('auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register('user', UserViewSet, basename='user')

# AUTHOR
routes.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    *routes.urls
]
