from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('create-account/', views.CreateAccountView.as_view(), name='create-account-page'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget-password-page'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password-page'),
]