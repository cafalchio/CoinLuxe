from django import forms
from django.core.exceptions import ValidationError

class AddToBagForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount



class RemoveFromBagForm(forms.Form):
    crypto_id = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount')
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount