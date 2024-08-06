from rest_framework import serializers
from .models import Pass, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PassSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        validated_data['user'] = user
        return super().create(validated_data)
