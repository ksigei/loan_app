from django.contrib import admin
from .models import Business, BusinessLocation, BankInformation, CreditCardInformation, LoanApplication, Loan, Repayment, Transaction

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_type', 'revenue', 'founding_date')
    search_fields = ('name', 'business_type')
    list_filter = ('business_type', 'revenue')
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'description', 'certificate_details', 'locations')
        }),
        ('Financial Information', {
            'fields': ('business_type', 'revenue', 'founding_date')
        }),
        ('Contact Information', {
            'fields': ('website', 'email', 'phone_number')
        }),
    )
    filter_horizontal = ('locations',)

@admin.register(BusinessLocation)
class BusinessLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country')
    search_fields = ('name', 'city', 'state', 'country')

@admin.register(BankInformation)
class BankInformationAdmin(admin.ModelAdmin):
    list_display = ('business', 'account_number')
    search_fields = ('business__name', 'account_number')

@admin.register(CreditCardInformation)
class CreditCardInformationAdmin(admin.ModelAdmin):
    list_display = ('business', 'card_number', 'expiry_date')
    search_fields = ('business__name', 'card_number')

@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('business', 'amount', 'purpose', 'status', 'created_at')
    search_fields = ('business__name', 'purpose', 'status')
    list_filter = ('status',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_application', 'amount', 'interest_rate', 'term_months')
    search_fields = ('loan_application__business__name',)
    list_filter = ('term_months',)

@admin.register(Repayment)
class RepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'installment_number', 'amount', 'due_date', 'paid')
    search_fields = ('loan__loan_application__business__name',)
    list_filter = ('paid',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'loan_application', 'amount', 'timestamp')
    search_fields = ('loan_application__business__name',)

