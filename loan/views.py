# In loans/views.py
from django.shortcuts import render, redirect
from .forms import BusinessForm, BankInformationForm, CreditCardInformationForm, LoanApplicationForm

def home(request):
    return render(request, 'home.html')

def step1(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
            return redirect('step2')
    else:
        form = BusinessForm()
    return render(request, 'step1.html', {'form': form})

def step2(request):
    if request.method == 'POST':
        form = BankInformationForm(request.POST)
        if form.is_valid():
            bank_info = form.save(commit=False)
            bank_info.business = request.user.business
            bank_info.save()
            return redirect('step3')
    else:
        form = BankInformationForm()
    return render(request, 'step2.html', {'form': form})

def step3(request):
    if request.method == 'POST':
        form = CreditCardInformationForm(request.POST)
        if form.is_valid():
            credit_card_info = form.save(commit=False)
            credit_card_info.business = request.user.business
            credit_card_info.save()
            return redirect('step4')
    else:
        form = CreditCardInformationForm()
    return render(request, 'step3.html', {'form': form})

def step4(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan_application = form.save(commit=False)
            loan_application.business = request.user.business
            loan_application.save()
            return redirect('loan_application_success')
    else:
        form = LoanApplicationForm()
    return render(request, 'step4.html', {'form': form})

def loan_application_success(request):
    return render(request, 'loan_application_success.html')
