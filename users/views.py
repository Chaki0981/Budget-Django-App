from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationUserForm

# Create your views here.

class LoginUserView(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('starting-page')
        else:
            messages.success(request, ("There was an error logging in!"))
            return redirect('login-page')
        
    def get(self, request):
        return render(request, 'users/login.html', {})
        
class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ("You were logged out!"))
        return redirect('starting-page')
    
class RegisterUserView(View):
    template_name = 'users/register.html'
    def get(self, request):
        form = RegistrationUserForm()

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request):
        form = RegistrationUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(user)
            messages.success(request, ("Registration successful!"))
            return redirect('starting-page')
        else:
            return render(request, 'users/register.html', {
                'form': form
            })