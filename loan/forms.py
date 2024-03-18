from django import forms
from .models import Business, BusinessLocation, BankInformation, CreditCardInformation, LoanApplication, Loan, Repayment, Transaction

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'certificate_details', 'business_type', 'revenue', 'founding_date', 'website', 'email', 'phone_number']

class BusinessLocationForm(forms.ModelForm):
    class Meta:
        model = BusinessLocation
        fields = ['name', 'address', 'city', 'state', 'country']

class BankInformationForm(forms.ModelForm):
    class Meta:
        model = BankInformation
        fields = ['account_number']

class CreditCardInformationForm(forms.ModelForm):
    class Meta:
        model = CreditCardInformation
        fields = ['card_number', 'cvv', 'expiry_date']

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['amount', 'purpose', 'repayment_start_time']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'interest_rate', 'term_months']

class RepaymentForm(forms.ModelForm):
    class Meta:
        model = Repayment
        fields = ['installment_number', 'amount', 'due_date', 'paid']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']
