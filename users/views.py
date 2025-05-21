from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # Verifica credenciales
            
            if user is not None:
                login(request, user) #Inicia sesión
                
                return redirect('home') # Redirije a la pagina principal
    
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request) # Cierra sesión
    return redirect('login') 