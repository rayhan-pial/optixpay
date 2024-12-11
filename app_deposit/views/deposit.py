from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Deposit
from .serializers import DepositSerializer

class CreateDepositAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveDepositAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            deposit = Deposit.objects.get(pk=pk)
        except Deposit.DoesNotExist:
            return Response({"error": "Deposit not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepositSerializer(deposit)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateDepositAPIView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            deposit = Deposit.objects.get(pk=pk)
        except Deposit.DoesNotExist:
            return Response({"error": "Deposit not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepositSerializer(deposit, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDepositAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            deposit = Deposit.objects.get(pk=pk)
        except Deposit.DoesNotExist:
            return Response({"error": "Deposit not found."}, status=status.HTTP_404_NOT_FOUND)

        deposit.delete()
        return Response({"message": "Deposit deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


