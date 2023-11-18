from django.db import models
from account.models import UserProfile
from django.utils import timezone


# Create your models here.
class Exam(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class ExamRegisteration(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.exam.title
    

