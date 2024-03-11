from django.urls import path
from .views import home, step1, step2, step3, step4, loan_application_success

urlpatterns = [
    path('', home, name='home'),  # URL pattern for the home view
    path('apply/step1/', step1, name='step1'),
    path('apply/step2/', step2, name='step2'),
    path('apply/step3/', step3, name='step3'),
    path('apply/step4/', step4, name='step4'),
    path('apply/success/', loan_application_success, name='loan_application_success'),
]
