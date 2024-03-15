from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from utils.hash import hash_generator


class Loan(models.Model):
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(_("Active"), default=True)
    value = models.DecimalField(_("Nominal Value"), max_digits=13, decimal_places=3)
    amount_of_payments = models.PositiveIntegerField(
        _("Amount of Payments"), default=12
    )
    interest_rate = models.DecimalField(
        _("Interest Rate"), max_digits=6, decimal_places=3
    )
    ip_address = models.CharField(_("IP Address"), max_length=45, null=True, blank=True)
    request_date = models.DateField(_("Request Date"), auto_now_add=True)
    bank = models.CharField(_("Bank"), max_length=100, null=True, blank=True)
    client = models.CharField(_("Client"), max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Loan {self.slug}"

    @property
    def payment_generated(self):
        return self.payments.exists()

    @property
    def amount_paid(self):
        if self.payment_generated:
            return self.payments.filter(
                is_paid=True, effective_date__isnull=False
            ).only("total_value", "effective_date").aggregate(
                total_value=Sum("total_value")
            )[
                "total_value"
            ] or Decimal(
                0.0
            )
        return Decimal(0.0)

    @property
    def amount_not_paid(self):
        if self.payment_generated:
            return self.payments.filter(
                is_paid=False, effective_date__isnull=True
            ).only("total_value", "effective_date").aggregate(
                total_value=Sum("total_value")
            )[
                "total_value"
            ] or Decimal(
                0.0
            )
        return Decimal(0.0)

    def save(self, *args, **kwargs):
        self.slug = self.slug or hash_generator()
        super(Loan, self).save(*args, **kwargs)
