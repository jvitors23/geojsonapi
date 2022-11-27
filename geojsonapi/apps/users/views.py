from django.contrib.auth import get_user_model
from rest_framework import authentication, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import AuthTokenSerializer, UserSerializer

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self) -> User:
        """Retrieve and return authenticated user"""
        return self.request.user
