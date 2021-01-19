#forms.py
from django import forms
from .models import Transaction

class TransactionStatusForm(forms.Form):
    status = forms.ChoiceField(
        required=True,
    )
    def form_action(self, transaction, status, user):
        print(user)
        return Transaction.update_transaction_status(
            id=transaction.transaction_id,status=status
        )