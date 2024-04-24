from django.urls import path

from users.apps import UsersConfig
from users.views import UserAuthAPIView, UserVerifyAPIView, UserAddInvitedCodeAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', UserAuthAPIView.as_view(), name='auth'),
    path('verify/', UserVerifyAPIView.as_view(), name='verify'),
    path('add_invited_code/', UserAddInvitedCodeAPIView.as_view(), name='add_invited_code'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
]
