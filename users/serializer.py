from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для модели Пользователя."""
    class Meta:
        model = User
        fields = "__all__"
