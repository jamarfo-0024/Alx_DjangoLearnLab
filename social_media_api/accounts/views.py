from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


User = get_user_model()


# =====================================
# REGISTER VIEW
# =====================================

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# =====================================
# LOGIN VIEW
# =====================================

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key,
                "user": UserSerializer(user).data
            })

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


# =====================================
# PROFILE VIEW
# =====================================

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# =====================================
# FOLLOW USER
# =====================================

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    user_to_follow = get_object_or_404(User, id=user_id)

    # Prevent following yourself
    if user_to_follow == request.user:
        return Response(
            {"error": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Prevent duplicate follows
    if user_to_follow in request.user.following.all():
        return Response({
            "message": f"You already follow {user_to_follow.username}"
        })

    request.user.following.add(user_to_follow)

    return Response({
        "message": f"You are now following {user_to_follow.username}"
    })


# =====================================
# UNFOLLOW USER
# =====================================

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    user_to_unfollow = get_object_or_404(User, id=user_id)

    if user_to_unfollow not in request.user.following.all():
        return Response({
            "message": f"You are not following {user_to_unfollow.username}"
        })

    request.user.following.remove(user_to_unfollow)

    return Response({
        "message": f"You unfollowed {user_to_unfollow.username}"
    })