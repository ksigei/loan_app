from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    certificate_details = models.FileField(upload_to='certificate_details/')

    def __str__(self):
        return self.name

class BankInformation(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Bank Information for {self.business.name}"

class CreditCardInformation(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Credit Card Information for {self.business.name}"

class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    repayment_start_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application for {self.business.name}"

class Loan(models.Model):
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_months = models.IntegerField()

    def __str__(self):
        return f"Loan {self.loan_application.business.name}"

class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    installment_number = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Repayment for {self.loan.loan_application.business.name}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction of {self.amount} for {self.loan_application.business.name}"
