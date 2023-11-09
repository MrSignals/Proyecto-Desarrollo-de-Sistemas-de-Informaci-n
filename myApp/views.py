from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def default(request):
    return render(request, 'default.html')

def home(request):
   return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html',{
        'form': UserCreationForm
    })

def products(request):
    return render(request, 'products.html')
