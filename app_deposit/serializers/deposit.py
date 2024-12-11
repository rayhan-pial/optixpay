from rest_framework import serializers
from app_deposit.models.deposit import Deposit

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'  # Include all fields of the Deposit model
