from django.urls import path
from . import views


urlpatterns = [
    path('login-user', views.LoginUserView.as_view(), name='login-page'),
    path('logout-user', views.LogoutUserView.as_view(), name='logout-page'),
    path('register-user', views.RegisterUserView.as_view(), name='register-page'),
]
