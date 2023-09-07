from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
def index (request):
    return render(request,"index.html")
def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST) # AuthenticationForm Bu form, kullanıcıların kimlik doğrulama (login) için kullanıcı adı (username) ve şifre (password) girmelerini sağlar.
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('index')
	form=AuthenticationForm()
	return render(request,"login.html",{'form':form})
