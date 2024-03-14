from apps.loan.models import Loan
from django.test import TestCase
from django.contrib.auth.models import User


class LoanModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )

    def setUp(self):
        self.loan = Loan.objects.create(
            user=self.user,
            value=1000,
            interest_rate=0.05,
            ip_address="192.168.1.1",
            bank="Test Bank",
            client="Test Client",
        )

    def test_loan_creation(self):
        self.assertTrue(isinstance(self.loan, Loan))
        self.assertEqual(self.loan.value, 1000)
        self.assertEqual(self.loan.interest_rate, 0.05)
        self.assertEqual(self.loan.ip_address, "192.168.1.1")
        self.assertEqual(self.loan.bank, "Test Bank")
        self.assertEqual(self.loan.client, "Test Client")
        self.assertTrue(self.loan.is_active)
        self.assertIsNotNone(self.loan.slug)

    def test_loan_str_method(self):
        self.assertEqual(str(self.loan), f"Loan {self.loan.slug}")

    def test_loan_slug_generation(self):
        loan = Loan.objects.create(
            user=self.user,
            value=2000,
            interest_rate=0.06,
            ip_address="192.168.1.2",
            bank="Another Bank",
            client="Another Client",
        )
        self.assertIsNotNone(loan.slug)

    def test_loan_blank_fields(self):
        loan = Loan.objects.create(user=self.user, value=3000)
        self.assertTrue(loan.is_active)
        self.assertIsNone(loan.ip_address)
        self.assertIsNone(loan.bank)
        self.assertIsNone(loan.client)

    def test_loan_unique_slug(self):
        loan1 = Loan.objects.create(user=self.user, value=4000)
        loan2 = Loan.objects.create(user=self.user, value=5000)
        self.assertNotEqual(loan1.slug, loan2.slug)

    def test_loan_user_relationship(self):
        self.assertEqual(self.loan.user, self.user)

    def test_loan_value_decimal_places(self):
        self.assertEqual(self.loan._meta.get_field("value").decimal_places, 3)

    def test_loan_interest_rate_decimal_places(self):
        self.assertEqual(self.loan._meta.get_field("interest_rate").decimal_places, 3)

    def test_loan_default_active(self):
        self.assertTrue(self.loan.is_active)
