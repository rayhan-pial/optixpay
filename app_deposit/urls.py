from django.urls import path
from app_deposit.views.deposit import (
    CreateDepositAPIView,
    RetrieveDepositAPIView,
    UpdateDepositAPIView,
    DeleteDepositAPIView
)

urlpatterns = [
    path('deposits/create/', CreateDepositAPIView.as_view(), name='create-deposit'),
    path('deposits/<int:pk>/', RetrieveDepositAPIView.as_view(), name='retrieve-deposit'),
    path('deposits/<int:pk>/update/', UpdateDepositAPIView.as_view(), name='update-deposit'),
    path('deposits/<int:pk>/delete/', DeleteDepositAPIView.as_view(), name='delete-deposit'),
]
