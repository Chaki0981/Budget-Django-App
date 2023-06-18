from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

from .models import Budget, Expense, Income, MonthlyBudget
from .forms import ExpenseForm, IncomeForm

# Create your views here.

class BudgetView():
    def calculate_budget(self, budget, incomes, expenses):
        incomes_list = [income.amount for income in incomes]
        expenses_list = [expense.amount for expense in expenses]
        budget.total_budget = sum(incomes_list)
        budget.total_expenses = sum(expenses_list)
        budget.available_budget = sum(incomes_list) - sum(expenses_list)
        budget.save()

class StartingPageView(View, BudgetView):
    template_name = 'budget/starting-page.html'

    def get(self, request):
        budget = Budget.objects.get(user=request.user)
        incomes = Income.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        self.calculate_budget(budget, incomes, expenses)
        context = {
            'budget': budget,
        }
        return render(request, self.template_name, context)

class MonthlyBudgetView(View, BudgetView):
    template_name = 'budget/monthly-budget.html'

    def form_handling(self, request):
        button_value = request.POST.get('form-button')
        if button_value == 'income':
            income = IncomeForm(request.POST)
            form = income.save(commit=False)
        elif button_value == 'expense':
            expense = ExpenseForm(request.POST)
            form = expense.save(commit=False)
        form.user = request.user
        form.save()

    def get(self, request, month):
        expense_form = ExpenseForm()
        income_form = IncomeForm()

        budget = Budget.objects.get(user=request.user)
        try:
            monthly_budget = MonthlyBudget.objects.get(user=request.user, month=month)
        except MonthlyBudget.DoesNotExist:
            monthly_budget = MonthlyBudget(month=month, user=request.user)

        con1 = Q(user=request.user)
        con2 = Q(month=month)
        incomes = Income.objects.filter(con1 & con2)
        expenses = Expense.objects.filter(con1 & con2)
        self.calculate_budget(budget, incomes, expenses)
        context = {
            'month': month,
            'expense_form': expense_form,
            'income_form': income_form,
            'budget': budget,
            'monthly_budget': monthly_budget,
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