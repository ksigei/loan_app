from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Business Name")
    description = models.TextField(verbose_name="Business Description")
    certificate_details = models.FileField(upload_to='certificate_details/', verbose_name="Certificate Details")
    locations = models.ManyToManyField('BusinessLocation', related_name='businesses', verbose_name="Business Locations")
    business_type = models.CharField(max_length=50, verbose_name="Business Type")
    revenue = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="Annual Revenue")
    founding_date = models.DateField(null=True, blank=True, verbose_name="Founding Date")
    website = models.URLField(max_length=200, blank=True, verbose_name="Business Website")
    email = models.EmailField(max_length=254, blank=True, verbose_name="Business Email")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Business Phone Number")

    def __str__(self):
        return self.name

class BusinessLocation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Location Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    country = models.CharField(max_length=100, verbose_name="Country")

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
    cvv = models.CharField(max_length=4)
    expiry_date = models.DateField()

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
