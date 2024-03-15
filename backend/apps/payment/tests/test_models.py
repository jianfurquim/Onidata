from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date, timedelta

from apps.payment.models import Payment
from apps.loan.models import Loan


class PaymentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        loan = Loan.objects.create(
            slug="test_loan",
            value=1000,
            interest_rate=0.5,
            amount_of_payments=1,
            user=user,
        )
        Payment.objects.create(
            slug="test_payment",
            loan=loan,
            value=1000,
            total_value=1005,
            interest_value=5,
            date=date.today(),
            due_date=date.today(),
            installment_number=1,
        )

    def test_make_payment(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.make_payment()
        self.assertTrue(payment.is_paid)

    def test_cancel_make_payment(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.cancel_make_payment()
        self.assertFalse(payment.is_paid)

    def test_slug_generation(self):
        payment = Payment.objects.get(slug="test_payment")
        self.assertIsNotNone(payment.slug)

    def test_total_value_calculation(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.make_payment()
        self.assertEqual(payment.total_value, Decimal(1005.0))

    def test_effective_date_update(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.make_payment()
        self.assertEqual(payment.effective_date, date.today())

    def test_cancel_make_payment_total_value(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.make_payment()
        payment.cancel_make_payment()
        self.assertEqual(payment.total_value, Decimal(1005.0))

    def test_save_generates_slug(self):
        loan = Loan.objects.get(slug="test_loan")
        payment = Payment.objects.create(
            loan=loan,
            value=100,
            total_value=105,
            interest_value=5,
            date=date.today(),
            due_date=date.today(),
            installment_number=1,
        )
        self.assertIsNotNone(payment.slug)

    def test_payment_value_calculation(self):
        payment = Payment.objects.get(slug="test_payment")
        self.assertEqual(payment.value, Decimal(1000))

    def test_payment_marked_as_paid(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.make_payment()
        self.assertTrue(payment.is_paid)

    def test_cancel_make_payment_no_effective_date_change(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.is_paid = False
        payment.save()
        payment.cancel_make_payment()
        self.assertIsNone(payment.effective_date)

    def test_save_updates_existing_payment(self):
        payment = Payment.objects.get(slug="test_payment")
        old_total_value = payment.total_value
        payment.total_value = 200
        payment.save()
        self.assertNotEqual(payment.total_value, old_total_value)

    def test_make_payment_late_updates_total_value(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.due_date = date.today() - timedelta(days=1)
        payment.save()
        payment.make_payment()
        self.assertGreater(payment.total_value, 105)

    def test_make_payment_early_no_total_value_update(self):
        payment = Payment.objects.get(slug="test_payment")
        payment.due_date = date.today() + timedelta(days=1)
        payment.save()
        payment.make_payment()
        self.assertEqual(payment.total_value, Decimal(1005.0))
