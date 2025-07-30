from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirmer le mot de passe")

    class Meta:
        model = CustomUser
        fields = [
          'id',
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'phone_number',
            'birth_date', 'blood_type', 'wilaya', 'is_donor'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # pas besoin d'enregistrer ce champ
        user = CustomUser.objects.create_user(**validated_data)
        return user
