import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

expire_delta = api_settings.REFRESH_TOKEN_LIFETIME
User = get_user_model()

class UserPublicSerializer():
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]
class UserRegisterSerializer(serializers.ModelSerializer):
    # password   = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password2'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'message',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, obj):
        return "Thank You For Registering. Please Verify Your  Email Before Continuing."
    def get_hey(self, obj):
        return "What is this get."
    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=20)

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Email Already exist")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Email Already exist")
        return value

    def get_token(self, obj):
        user = obj
        refresh = RefreshToken.for_user(user)
        result = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return result

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Password must match")
        return data

    def create(self, validated_data):
        user_obj = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()

        return user_obj
