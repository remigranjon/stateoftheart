from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
# from django.views import generic


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
# Create your views here.

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('blog:home')
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    form = UserForm(instance = request.user)
    return render(request, 'accounts/profile.html', {'form' : form, 'user': request.user})

def logoutView(request):
    logout(request)
    return redirect('accounts:logged_out')

def logged_out(request):
    return render(request, 'registration/logged_out.html')