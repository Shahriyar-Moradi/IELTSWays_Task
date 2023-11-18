from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Exam,ExamRegisteration
from .serializers import (
ExamSerializer,
ExamRegisterationSerializer
# ,ExamWithdrawalSerializer
)
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from django.contrib.auth import authenticate,login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
import re
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from ippanel import Client
from ippanel import HTTPError, Error, ResponseCode
from rest_framework import viewsets
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication



class ExamregisterationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = ExamRegisteration.objects.all()
    serializer_class =ExamRegisterationSerializer

    def post(self, request):
        user = self.request.user
        request.data['user'] = user.id
        exam=request.data.get('exam')
        
        if ExamRegisteration.objects.filter(user=user,exam=exam).exists():
            return Response({'message': 'user has registerated already.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ExamRegisterationSerializer(data=request.data)
        if serializer.is_valid():
            user.exam_registered=True
            user.save()
            serializer.save()
            status_code = status.HTTP_201_CREATED
            return Response(serializer.data, status=status_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get(self, request, *args, **kwargs):
        
    #     queryset = ExamRegisteration.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)
    
    
    
class ExamWithdrawalRegisterationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = ExamRegisteration.objects.all()
    serializer_class =ExamRegisterationSerializer

    def post(self, request):
        user = self.request.user
        exam_id = request.data.get('exam')

        try:
            exam_registration = ExamRegisteration.objects.get(user=user, exam=exam_id, user__exam_registered=True, user__exam_withdrawal=False)
        except ExamRegisteration.DoesNotExist:
            return Response({'message': 'User has not registered for the exam.'}, status=status.HTTP_400_BAD_REQUEST)

        if exam_registration.user.exam_withdrawal:
            return Response({'message': 'User has withdrawn already.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ExamRegisterationSerializer(exam_registration, data={'user': user.id, **request.data})
        if serializer.is_valid():
            # Update user fields
            user.exam_registered = False
            user.exam_withdrawal = True
            user.save()

            # Save the serializer instance
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ExamView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class =ExamSerializer
    
    
    
    
    
# class WithdrawalExamView(generics.ListAPIView):
#     queryset = ExamRegisteration.objects.filter(user__exam_withdrawal=True).select_related('user').distinct('user')
#     serializer_class =ExamRegisterationSerializer

class WithdrawalListView(APIView):
    serializer_class =ExamRegisterationSerializer
    def get(self, request, *args, **kwargs):
        # Assuming ExamRegisteration has a ForeignKey to User model
        withdrawals = ExamRegisteration.objects.filter(user__exam_withdrawal=True).select_related('user')
        # withdrawals = ExamRegisteration.objects.filter(user__exam_withdrawal=True).select_related('user').distinct('user')
        serializer = ExamRegisterationSerializer(withdrawals, many=True)
        return Response(serializer.data)
    

class ExamRegisterationViewSet(viewsets.ViewSet):
    queryset = ExamRegisteration.objects.all()
    serializer_class = ExamRegisterationSerializer

    @extend_schema(description="Retrieve a list of registeration.",responses=ExamRegisterationSerializer)
    def list(self, request):
        data = self.queryset
        serializer = self.serializer_class(self.queryset.filter(user__exam_registered=True), many=True)
        # serializer = self.serializer_class(data, many=True)
        response = Response(serializer.data, status=200)
        # Add debug print statements here
        # print("Data:", data)
        # print("Serialized Data:", serializer.data)
        return response
    
    # def retrieve(self,request,pk):
    #     serializer= ServiceSerializer(self.queryset.filter(id=pk),many=True)
    #     response=Response(serializer.data)
    #     return response
        
    
    @action(methods=['get'], detail=False, url_path=r"(?P<exam_id>\w+)/all")
    def list_register_by_exam(self, request, exam_id):
        serializer = ExamRegisterationSerializer(self.queryset.filter(exam=exam_id), many=True)

        return Response(serializer.data)
    

        
