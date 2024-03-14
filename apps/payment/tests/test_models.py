from django.db import IntegrityError

from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from apps.payment.models import Payment
from apps.loan.models import Loan


class PaymentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )

        self.loan = Loan.objects.create(
            user=self.user, value=1000, interest_rate=0.05, request_date=date.today()
        )

        self.payment = Payment.objects.create(
            loan=self.loan,
            value=200,
            total_value=220,
            interest_value=20,
            date=date.today(),
            due_date=date.today(),
            installment_number=1,
            is_paid=False,
        )

    def test_payment_creation(self):
        self.assertIsInstance(self.payment, Payment)
        self.assertEqual(self.payment.loan, self.loan)
        self.assertEqual(self.payment.value, 200)
        self.assertEqual(self.payment.total_value, 220)
        self.assertEqual(self.payment.interest_value, 20)
        self.assertEqual(self.payment.date, date.today())
        self.assertEqual(self.payment.due_date, date.today())
        self.assertEqual(self.payment.installment_number, 1)
        self.assertFalse(self.payment.is_paid)

    def test_str_method(self):
        expected_str = f"Payment for Loan {self.loan.slug} on {date.today()}"
        self.assertEqual(str(self.payment), expected_str)

    def test_payment_save(self):
        saved_payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(saved_payment.loan, self.loan)
        self.assertEqual(saved_payment.value, 200)
        self.assertEqual(saved_payment.total_value, 220)
        self.assertEqual(saved_payment.interest_value, 20)
        self.assertEqual(saved_payment.date, date.today())
        self.assertEqual(saved_payment.due_date, date.today())
        self.assertEqual(saved_payment.installment_number, 1)
        self.assertFalse(saved_payment.is_paid)

    def test_payment_creation_multiple(self):
        payment2 = Payment.objects.create(
            loan=self.loan,
            value=300,
            total_value=330,
            interest_value=30,
            date=date.today(),
            due_date=date.today(),
            installment_number=2,
            is_paid=False,
        )
        payment3 = Payment.objects.create(
            loan=self.loan,
            value=400,
            total_value=440,
            interest_value=40,
            date=date.today(),
            due_date=date.today(),
            installment_number=3,
            is_paid=False,
        )
        self.assertIsInstance(payment2, Payment)
        self.assertIsInstance(payment3, Payment)

    def test_payment_update(self):
        self.payment.value = 250
        self.payment.save()
        updated_payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(updated_payment.value, 250)

    def test_payment_deletion(self):
        payment_id = self.payment.id
        self.payment.delete()
        with self.assertRaises(Payment.DoesNotExist):
            Payment.objects.get(id=payment_id)

    def test_installment_number_default(self):
        new_payment = Payment.objects.create(
            loan=self.loan,
            value=150,
            total_value=165,
            interest_value=15,
            date=date.today(),
            due_date=date.today(),
        )
        self.assertEqual(new_payment.installment_number, 1)

    def test_payment_is_paid(self):
        self.payment.is_paid = True
        self.payment.save()
        updated_payment = Payment.objects.get(id=self.payment.id)
        self.assertTrue(updated_payment.is_paid)

    def test_payment_uniqueness(self):
        with self.assertRaises(IntegrityError):
            Payment.objects.create(
                slug=self.payment.slug,
                loan=self.loan,
                value=300,
                total_value=330,
                interest_value=30,
                date=date.today(),
                due_date=date.today(),
                installment_number=2,
                is_paid=False,
            )

    def test_payment_queryset(self):
        queryset = Payment.objects.filter(loan=self.loan)
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first(), self.payment)

    def test_payment_date(self):
        payment = Payment.objects.get(pk=1)
        self.assertTrue(payment.date)

    def test_payment_due_date(self):
        payment = Payment.objects.get(pk=1)
        self.assertTrue(payment.due_date)

    def test_payment_value_max_digits(self):
        payment = Payment.objects.get(pk=1)
        max_digits = payment._meta.get_field("value").max_digits
        self.assertEqual(max_digits, 13)

    def test_payment_value_decimal_places(self):
        payment = Payment.objects.get(pk=1)
        decimal_places = payment._meta.get_field("value").decimal_places
        self.assertEqual(decimal_places, 3)

    def test_payment_total_value_max_digits(self):
        payment = Payment.objects.get(pk=1)
        max_digits = payment._meta.get_field("total_value").max_digits
        self.assertEqual(max_digits, 13)

    def test_payment_total_value_decimal_places(self):
        payment = Payment.objects.get(pk=1)
        decimal_places = payment._meta.get_field("total_value").decimal_places
        self.assertEqual(decimal_places, 3)

    def test_payment_interest_value_max_digits(self):
        payment = Payment.objects.get(pk=1)
        max_digits = payment._meta.get_field("interest_value").max_digits
        self.assertEqual(max_digits, 13)

    def test_payment_interest_value_decimal_places(self):
        payment = Payment.objects.get(pk=1)
        decimal_places = payment._meta.get_field("interest_value").decimal_places
        self.assertEqual(decimal_places, 3)

    def test_payment_installment_number_positive(self):
        payment = Payment.objects.get(pk=1)
        self.assertGreaterEqual(payment.installment_number, 0)

    def test_payment_is_paid_boolean(self):
        payment = Payment.objects.get(pk=1)
        self.assertIsInstance(payment.is_paid, bool)
