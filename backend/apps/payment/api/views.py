from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction

from apps.payment.api.serializers import PaymentSerializer
from apps.payment.models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            try:
                return Payment.objects.filter(loan__user__id=user_id)
            except Payment.DoesNotExist:
                return Payment.objects.none()
        else:
            return Payment.objects.none()

    @action(detail=True, methods=["post"])
    def make_payment(self, request, pk=None):
        payment = self.get_object()

        if not payment:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            with transaction.atomic():
                payment.make_payment()
                return Response(
                    {"message": "Payment confirmed successfully"},
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
