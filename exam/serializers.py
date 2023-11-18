# serializers.py

from rest_framework import serializers
from account.models import UserProfile
from.models import ExamRegisteration,Exam

class ExamSerializer(serializers.ModelSerializer):
    exam_title=serializers.CharField(source='title')
    class Meta:
        model = Exam
        fields = ['exam_title','description']
        
        
class ExamRegisterationSerializer(serializers.ModelSerializer):
    # exam =ExamSerializer()
    class Meta:
        model = ExamRegisteration
        fields = ['user','exam','date']
        
        
# class ExamWithdrawalSerializer(serializers.ModelSerializer):
#     # exam =ExamSerializer()
#     class Meta:
#         model = ExamRegisteration
#         fields = ['user','exam']


