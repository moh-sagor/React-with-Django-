from rest_framework.viewsets import ModelViewSet

from BurgerApi.models import UserProfile
from BurgerApi.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
