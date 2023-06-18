from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

class Income(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes", null=True)

    def __str__(self):
        return f'{self.title}, {self.amount} - {self.date}'

class Budget(models.Model):


    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budget", null=True)

    def __str__(self):
        return f'User = {self.user} - {self.total_budget}'

class MonthlyBudget(models.Model):
    JAN = "JANUARY"
    FEB = "FEBRUARY"
    MAR = "MARCH"
    APR = "APRIL"
    MAY = "MAY"
    JUN = "JUNE"
    JUL = "JULY"
    AUG = "AUGUST"
    SEP = "SEPTEMBER"
    OCT = "OCTEMBER"
    NOV = "NOVEMBER"
    DEC = "DECEMBER"

    MONTH_CHOICES = (
        (JAN, "January"),
        (FEB, "February"),
        (MAR, "March"),
        (APR, "April"),
        (MAY, "May"),
        (JUN, "June"),
        (JUL, "July"),
        (AUG, "August"),
        (SEP, "September"),
        (OCT, "October"),
        (NOV, "November"),
        (DEC, "December"),
    )

    month = models.CharField(max_length=20, choices=MONTH_CHOICES, default=JAN)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="monthly_budgets", null=True)

    def __str__(self):
        return f'User = {self.user} - {self.total_budget} - month {self.month}'
    
class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount [PLN]')
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="expenses", blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses", null=True)

    def __str__(self):
        return f'{self.title}'
