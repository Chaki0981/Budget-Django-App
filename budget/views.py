from django.shortcuts import render, redirect
from django.views import View
from .models import Budget, Expense
from .forms import ExpenseForm, IncomeForm

# Create your views here.

class StartingPageView(View):
    template_name = 'budget/starting-page.html'

    def form_handling(self, request, budget):
        button_value = request.POST.get('form-button')
        if button_value == 'income':
            form = IncomeForm(request.POST)
            form.save()
            amount = form.cleaned_data['amount']
            budget.total_budget += amount
            budget.availabe_budget += amount
        elif button_value == 'expense':
            form = ExpenseForm(request.POST)
            form.save()
            amount = form.cleaned_data['amount']
            budget.total_expenses += amount
            budget.availabe_budget -= amount
        budget.save()
        

    def get(self, request):
        expense_form = ExpenseForm()
        income_form = IncomeForm()
        budget = Budget.objects.get(id=1)
        context = {
            'expense_form': expense_form,
            'income_form': income_form,
            'budget': budget,
            'expenses': Expense.objects.all().order_by('date')
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        budget = Budget.objects.get(id=1)
        self.form_handling(request, budget)

        return redirect('starting-page')
