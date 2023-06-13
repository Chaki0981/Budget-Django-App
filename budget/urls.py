from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('expense/<int:id>', views.ExpenseDetailsView.as_view(), name='expense-details-page')
]
