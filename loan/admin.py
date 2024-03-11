from django.contrib import admin
from .models import Business, BankInformation, CreditCardInformation, LoanApplication, Loan, Repayment, Transaction

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

class BankInformationAdmin(admin.ModelAdmin):
    list_display = ['business', 'account_number']
    search_fields = ['business__name']

class CreditCardInformationAdmin(admin.ModelAdmin):
    list_display = ['business', 'card_number']
    search_fields = ['business__name']

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ['business', 'amount', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['business__name', 'amount']
    date_hierarchy = 'created_at'

class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_application', 'amount', 'interest_rate', 'term_months']
    search_fields = ['loan_application__business__name']

class RepaymentAdmin(admin.ModelAdmin):
    list_display = ['loan', 'installment_number', 'amount', 'due_date', 'paid']
    search_fields = ['loan__loan_application__business__name']
    list_filter = ['paid']
    date_hierarchy = 'due_date'

from django.contrib import admin
from .models import Business, BankInformation, CreditCardInformation, LoanApplication, Loan, Repayment, Transaction

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

class BankInformationAdmin(admin.ModelAdmin):
    list_display = ['business', 'account_number']
    search_fields = ['business__name']

class CreditCardInformationAdmin(admin.ModelAdmin):
    list_display = ['business', 'card_number']
    search_fields = ['business__name']

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ['business', 'amount', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['business__name', 'amount']
    date_hierarchy = 'created_at'

class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_application', 'amount', 'interest_rate', 'term_months']
    search_fields = ['loan_application__business__name']

class RepaymentAdmin(admin.ModelAdmin):
    list_display = ['loan', 'installment_number', 'amount', 'due_date', 'paid']
    search_fields = ['loan__loan_application__business__name']
    list_filter = ['paid']
    date_hierarchy = 'due_date'

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'loan_application_business_name', 'amount', 'timestamp']
    search_fields = ['loan_application__business__name', 'user__username']
    date_hierarchy = 'timestamp'

    def loan_application_business_name(self, obj):
        return obj.loan_application.business.name if obj.loan_application else 'N/A'

    loan_application_business_name.short_description = 'Business Name'

admin.site.register(Business, BusinessAdmin)
admin.site.register(BankInformation, BankInformationAdmin)
admin.site.register(CreditCardInformation, CreditCardInformationAdmin)
admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Repayment, RepaymentAdmin)
admin.site.register(Transaction, TransactionAdmin)

