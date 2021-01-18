import uuid
from django.db import models

# Create your models here.
class Transaction(models.Model):
    user_to_status_map = {}
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique TransactionId for this transaction')
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    merchant_name = models.CharField(max_length=200)
    issuing_bank = models.CharField(max_length=200)
    merchant_bank = models.CharField(max_length=200)
    authorized_count = models.BigIntegerField(default=0)
    reject_count = models.BigIntegerField(default=0)
    flag_count = models.BigIntegerField(default=0)

    TRANSACTION_STATUS = (
        ('A', 'Authorized'),
        ('R', 'Reject'),
        ('F', 'Flag'),
    )
    status = models.CharField(
        max_length=1,
        choices=TRANSACTION_STATUS,
        blank=True,
        default='m',
        help_text='Status of Transaction',
    )
    def __str__(self):
        """String for representing the Model object."""
        return "Transaction id:  %s " % self.transaction_id

    def update_transaction_status(self,id):
        self.user_to_status_map = {}
        print(self.transaction_id)
