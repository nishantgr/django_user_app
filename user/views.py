from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print ("Valid form", request.POST)
            form.save()
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request,
            template_name='user/register.html',
            context={'form': form})

def home(request):
    return render(request, template_name='user/home.html',
                context={'user':request.user})
