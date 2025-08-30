from rest_framework import serializers
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email',
            'first_name', 'last_name', 'phone_number',
            'birth_date', 'blood_type', 'wilaya', 'is_donor']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',
            'first_name', 'last_name', 'phone_number',
            'birth_date', 'blood_type', 'wilaya', 'is_donor']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
