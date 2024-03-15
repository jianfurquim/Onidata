from rest_framework import serializers
from apps.payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    client = serializers.ReadOnlyField(source="loan.client")
    bank = serializers.ReadOnlyField(source="loan.bank")

    class Meta:
        model = Payment
        fields = [
            "pk",
            "loan",
            "client",
            "bank",
            "value",
            "total_value",
            "interest_value",
            "date",
            "due_date",
            "effective_date",
            "is_paid",
        ]
