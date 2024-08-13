from rest_framework import serializers
from .models import Pass, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PassSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user, created = User.objects.get_or_create(**user_data)
        validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Отключаем обновление пользователя в PATCH-запросе
        validated_data.pop('user', None)
        return super().update(instance, validated_data)
