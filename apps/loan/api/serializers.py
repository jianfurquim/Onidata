from rest_framework import serializers
from apps.loan.models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"
