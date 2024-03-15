from rest_framework import serializers
from apps.loan.models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "pk",
            "value",
            "amount_of_payments",
            "interest_rate",
            "ip_address",
            "request_date",
            "client",
            "bank",
        ]
