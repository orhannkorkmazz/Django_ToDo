from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm ,LoginForm
def index (request):
    return render(request,"index.html")
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Böyle bir kullanıcı bulunmuyor ya da şifre yanlış")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return render(request,"index.html")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request) 
    return render(request,"index.html")
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username =username)
            newUser.set_password(password)
            newUser.save()
            #login(request,newUser)
            messages.success(request,"Başarıyla kayıt oldunuz.")
            return render(request,"login.html",{'form':form})
    else:
        context = {
            "form" : form
        } 
    return render(request,"register.html",context)

	
