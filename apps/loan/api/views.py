from dateutil.relativedelta import relativedelta
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.loan.models import Loan
from apps.loan.api.serializers import LoanSerializer
from django.db import transaction

from apps.payment.models import Payment


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def generate_payments(self, request, pk=None):
        loan = self.get_object()

        try:
            with transaction.atomic():
                for i in range(1, loan.amount_of_payments + 1):
                    due_date = loan.request_date + relativedelta(months=i)
                    value = loan.value / loan.amount_of_payments
                    interest_value = value * (loan.interest_rate / 100)
                    total_value = value + interest_value

                    Payment.objects.create(
                        loan=loan,
                        value=value,
                        interest_value=interest_value,
                        total_value=total_value,
                        date=loan.request_date,
                        due_date=due_date,
                        installment_number=i,
                        is_paid=False,
                    )

            return Response({"response": "success"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
