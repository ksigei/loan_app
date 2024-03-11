from django import forms
from .models import LoanApplication, Business, BankInformation, CreditCardInformation

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'certificate_details']

class BankInformationForm(forms.ModelForm):
    class Meta:
        model = BankInformation
        fields = ['account_number']

class CreditCardInformationForm(forms.ModelForm):
    class Meta:
        model = CreditCardInformation
        fields = ['card_number']

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['amount', 'purpose', 'repayment_start_time']
