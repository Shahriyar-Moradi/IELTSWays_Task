# urls.py

from django.urls import path
from .views import UserProfileRegistrationView,UserLoginView

urlpatterns = [
    path('register/', UserProfileRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    # Add other URLs as needed
]
