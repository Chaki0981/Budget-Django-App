from django.contrib import admin
from .models import Budget, Expense, Category, Income

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'user')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'user')


admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
