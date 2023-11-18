# managers.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

# class UserProfileManager(BaseUserManager):
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserProfileManager(BaseUserManager):
    def create_user(self, first_name, last_name, national_id, password=None, **extra_fields):
        # email = self.normalize_email(email)
        user = self.model( first_name=first_name, last_name=last_name, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, **extra_fields)
    
    
    '''neww'''
    
    # def create_user(self, national_id, first_name, last_name, password=None, **extra_fields):
    #     user = self.model(national_id=national_id, first_name=first_name, last_name=last_name, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     return self.create_user(email, password=password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    national_id = models.CharField(max_length=20, unique=True)  # Make national_id unique
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    exam_withdrawal=models.BooleanField(default=False)
    exam_registered=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'national_id'  # Change the login field to national_id
    REQUIRED_FIELDS = ['first_name', 'last_name','email'] # Add other required fields

    def __str__(self):
        return self.national_id
