from django.shortcuts import render, redirect
from django.views import View
from .models import Budget, Expense, Income
from .forms import ExpenseForm, IncomeForm

# Create your views here.

class StartingPageView(View):
    template_name = 'budget/starting-page.html'

    def calculate_budget(self, budget, incomes, expenses):
        incomes_list = [income.amount for income in incomes]
        expenses_list = [expense.amount for expense in expenses]
        budget.total_budget = sum(incomes_list)
        budget.total_expenses = sum(expenses_list)
        budget.available_budget = sum(incomes_list) - sum(expenses_list)
        budget.save()


    def form_handling(self, request):
        button_value = request.POST.get('form-button')
        if button_value == 'income':
            form = IncomeForm(request.POST)
        elif button_value == 'expense':
            form = ExpenseForm(request.POST)
        form.save()
        

    def get(self, request):
        expense_form = ExpenseForm()
        income_form = IncomeForm()
        budget = Budget.objects.get(id=1)
        incomes = Income.objects.all()
        expenses = Expense.objects.all()
        self.calculate_budget(budget, incomes, expenses)
        context = {
            'expense_form': expense_form,
            'income_form': income_form,
            'budget': budget,
            'expenses': expenses.order_by('date'),
            'incomes': incomes.order_by('date'),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        self.form_handling(request)
        return redirect('starting-page')

class ExpenseDetailsView(View):
    template_name = 'budget/expense-details.html'
    def get(self, request, id):
        expense = Expense.objects.get(pk=id)
        form = ExpenseForm(instance=expense)

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)