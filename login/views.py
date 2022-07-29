from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm



from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponse("signup.html")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def home(request):
    return render(request,'home.html')


@csrf_protect
def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is invalid'})

    else:
        return render(request,'login.html')

def logout(request):
    return redirect('login')