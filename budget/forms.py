from django import forms
from .models import Expense, Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['date', 'user']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ['user']