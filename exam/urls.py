
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import(ExamregisterationView,ExamView,ExamRegisterationViewSet
                ,WithdrawalListView
                #    WithdrawalExamView,
                ,ExamWithdrawalRegisterationView
                   )

router = DefaultRouter()
router.register(r'list_registerations',ExamRegisterationViewSet )



urlpatterns = [
    path('', include(router.urls)),
    path('exam_list', ExamView.as_view(), name='exam_list'),
    path('exam_registeration/', ExamregisterationView.as_view(), name='exam_registeration'),
    path('exam_withdrawal_registeration/', ExamWithdrawalRegisterationView.as_view(), name='exam_withdrawal_registeration'),
    # path('exam_withdrawal/', WithdrawalExamView.as_view(), name='exam_withdrawal'),
    path('exam_withdrawal/', WithdrawalListView.as_view(), name='exam_withdrawal'),
    # path('registeration_list/', GetExamregisterationView.as_view(), name='registeration_list'),
    path('registeration_list/', ExamRegisterationViewSet.as_view({''}), name='registeration_list'),
    # Add other URLs as needed
]




