from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('User authenticated successfully!')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout_view(request):
    logout(request)
    return HttpResponse('User logged out successfully!')