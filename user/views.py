from django.shortcuts import render
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
    else:
        form = UserRegisterForm()
    return render(request,
            template_name='user/register.html',
            context={'form': form})

def home(request):
    pass
