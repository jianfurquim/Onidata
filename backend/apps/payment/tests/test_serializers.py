from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date

from django.utils.dateparse import parse_date

from apps.loan.models import Loan
from apps.payment.models import Payment
from apps.payment.api.serializers import PaymentSerializer


class PaymentSerializerTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        loan = Loan.objects.create(
            slug="test_loan",
            value=1000,
            interest_rate=0.5,
            amount_of_payments=1,
            user=user,
        )
        self.payment = Payment.objects.create(
            loan=loan,
            value=1000,
            total_value=1005,
            interest_value=5,
            date=date.today(),
            due_date=date.today(),
            effective_date=date.today(),
            is_paid=False,
        )
        self.serializer = PaymentSerializer(instance=self.payment)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            [
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
            ],
        )

    def test_loan_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.payment.loan_id, data["loan"])

    def test_value_field_content(self):
        data = self.serializer.data
        serialized_interest_value = Decimal(data["value"])
        self.assertEqual(self.payment.value, serialized_interest_value)

    def test_total_value_field_content(self):
        data = self.serializer.data
        serialized_interest_value = Decimal(data["total_value"])
        self.assertEqual(self.payment.total_value, serialized_interest_value)

    def test_interest_value_field_content(self):
        data = self.serializer.data
        serialized_interest_value = Decimal(data["interest_value"])
        self.assertEqual(self.payment.interest_value, serialized_interest_value)

    def test_date_field_content(self):
        data = self.serializer.data
        serialized_date = parse_date(data["date"])
        self.assertEqual(self.payment.date, serialized_date)

    def test_due_date_field_content(self):
        data = self.serializer.data
        serialized_date = parse_date(data["due_date"])
        self.assertEqual(self.payment.due_date, serialized_date)

    def test_effective_date_field_content(self):
        data = self.serializer.data
        serialized_date = parse_date(data["effective_date"])
        self.assertEqual(self.payment.effective_date, serialized_date)

    def test_is_paid_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.payment.is_paid, data["is_paid"])
