
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import (UserProfileSerializer,LoginSerializer
,UserRegisterSerializer
)
from django.contrib.auth import authenticate,login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializers import CustomTokenObtainPairSerializer
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication



class UserProfileRegistrationView(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        national_id = request.data.get('national_id')
        password = request.data.get('password')

        # Check if username already exists
        if UserProfile.objects.filter(national_id=national_id).exists():
            return Response({'message': 'national id is already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if email already exists
        # if UserProfile.objects.filter(email=email).exists():
        #     return Response({'message': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check password length
        if len(password) < 4:
            return Response({'message': 'Password must be at least 4 characters long.'}, status=status.HTTP_400_BAD_REQUEST)

        user = UserProfile.objects.create_user(first_name=first_name,last_name=last_name, password=password,national_id=national_id)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response(
            {
                "user_id": user.id,
                "message": f" User registration successful",
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    serializer_class = LoginSerializer  # Specify the serializer class

    def post(self, request):
        national_id = request.data.get('national_id')
        password = request.data.get('password')

        user = authenticate(request,national_id=national_id, password=password)

        if user is not None:
            login(request, user)
            # if user.is_active:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response({'message': 'Login successful', 'access_token': access_token,'user':user.id}, status=status.HTTP_200_OK)
            # else:
            #     return Response({'message': 'Account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Invalid national_id or password.'}, status=status.HTTP_401_UNAUTHORIZED)


