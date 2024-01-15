from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.views import generic

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chess:chess')    
    return render(request, 'registration/register.html', { 'form': form}) 

class sign_in(LoginView):
    form_class = LoginForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy("chess")
    template_name: str = "registration/login.html"