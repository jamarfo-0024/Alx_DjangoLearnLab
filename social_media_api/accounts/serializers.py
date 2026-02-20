from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


# ==============================
# User Registration Serializer
# ==============================

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'bio',
            'profile_picture'
        ]

    def create(self, validated_data):

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )

        # create auth token automatically
        Token.objects.create(user=user)

        return user


# ==============================
# Login Serializer
# ==============================

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


# ==============================
# User Profile Serializer
# ==============================

class UserSerializer(serializers.ModelSerializer):

    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'bio',
            'profile_picture',
            'followers_count',
            'following_count'
        ]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()