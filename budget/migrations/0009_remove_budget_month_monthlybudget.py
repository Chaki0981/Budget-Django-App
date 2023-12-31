# Generated by Django 4.1.5 on 2023-06-18 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0008_expense_user_income_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='month',
        ),
        migrations.CreateModel(
            name='MonthlyBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('JANUARY', 'January'), ('FEBRUARY', 'February'), ('MARCH', 'March'), ('APRIL', 'April'), ('MAY', 'May'), ('JUNE', 'June'), ('JULY', 'July'), ('AUGUST', 'August'), ('SEPTEMBER', 'September'), ('OCTEMBER', 'October'), ('NOVEMBER', 'November'), ('DECEMBER', 'December')], default='JANUARY', max_length=20)),
                ('total_budget', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('available_budget', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_expenses', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monthly_budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
