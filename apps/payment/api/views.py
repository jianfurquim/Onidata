from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.payment.api.serializers import PaymentSerializer
from apps.payment.models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
