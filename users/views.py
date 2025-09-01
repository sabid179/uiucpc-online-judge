from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

class LoginView(FormView):
    template_name = 'users/login-page.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  # Replace 'home' with your desired redirect

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
    
class CreateAccountView(FormView):
    template_name = 'users/create-account-page.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ForgetPasswordView(TemplateView):
    template_name = 'users/forget-password-page.html'
    
class ResetPasswordView(TemplateView):
    template_name = 'users/reset-password-page.html'