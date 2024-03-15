from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.loan.models import Loan
from utils.hash import hash_generator
from datetime import date


class Payment(models.Model):
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    value = models.DecimalField(_("Payment Value"), max_digits=13, decimal_places=3)
    total_value = models.DecimalField(_("Total Value"), max_digits=13, decimal_places=3)
    interest_value = models.DecimalField(
        _("Interest Value"), max_digits=13, decimal_places=3
    )
    date = models.DateField(_("Payment Date"))
    due_date = models.DateField(_("Due Date"))
    effective_date = models.DateField(_("Effective Date"), blank=True, null=True)
    installment_number = models.PositiveIntegerField(_("Installment Number"), default=1)
    is_paid = models.BooleanField(_("Is Paid"), default=False)

    def __str__(self):
        return f"Payment for Loan {self.loan.slug} on {self.due_date}"

    def make_payment(self):
        self.is_paid = True
        self.effective_date = date.today()

        if self.effective_date > self.due_date:
            days_difference = abs((self.due_date - self.effective_date).days)
            interest_rate_per_day = self.loan.interest_rate / 100 / 365
            interest_factor = pow(1 + interest_rate_per_day, days_difference)
            self.total_value = self.total_value * interest_factor

        self.save()

    def cancel_make_payment(self):
        self.is_paid = False
        self.effective_date = None

        value = self.loan.value / self.loan.amount_of_payments
        interest_value = value * (self.loan.interest_rate / 100)
        self.total_value = value + interest_value

        self.save()

    def save(self, *args, **kwargs):
        self.slug = self.slug or hash_generator()
        super(Payment, self).save(*args, **kwargs)
