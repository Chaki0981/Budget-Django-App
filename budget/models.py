from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

class Income(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.amount} - {self.date}'

class Budget(models.Model):
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    available_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'id = {self.pk} - {self.total_budget}'

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount [PLN]')
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="expenses", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
