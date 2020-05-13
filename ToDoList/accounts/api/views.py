from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .permissions import AnonPermissionOnly
from django.contrib.auth.models import User, auth
# models.User

# User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]


class AuthAPIView(APIView):
    # authentication_classes = []
    permission_classes = [permissions.AllowAny]  # permissions.AllowAny

    def post(self, request, *args, **kwargs):
        print(str(request.data))
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        print(data)
        username = data.get('username')
        password = data.get('password')
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                result = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(result)
            else:
                return Response({"detail": "Invalid credentials "}, status=401)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials "}, status=401)
        
        ''' 
        qs = User._default_manager.filter(
            Q(**{User.USERNAME_FIELD: username}
              ) | Q(email__iexact=username)
        )
        print(qs.count())
        print(username)
        if qs.count() > 1:
            user_obj = qs.first()
            print(user_obj)
            if user_obj.check_password(password):
                user = user_obj
                print(user)
                refresh = RefreshToken.for_user(user)
                result = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                print(result)
                return Response(result)
        return Response({"detail": "Invalid credentials "}, status=401) 
        '''
