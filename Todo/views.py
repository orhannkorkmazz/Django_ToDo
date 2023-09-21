from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm ,LoginForm,TodoForm
from .models import Todo
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
            return redirect("/login/")
    else:
        context = {
            "form" : form
        } 
    return render(request,"register.html",context)
def dashboard(request):
    todos=Todo.objects.filter(author=request.user)
    form=TodoForm
    context={
        "todos":todos,
        "form":form
    }
    return render(request,"dashboard.html",context)
def addtodo(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        todos=form.save(commit=False)#sadece form.save() yaparak kayıt işlemi gerçekleşebilir fakat bu formdan alınan bilgide yazar bilgisi olduğu için ve biz makalede sadece başlık ve içerik bilgisi istediğimizi için hata ile karşılaşırız 
        todos.author=request.user
        todos.save()
        return redirect("/dashboard/")
    
    return render(request,"addtodo.html",{"form":form} )
def deletetodo(request,id):
    todo = get_object_or_404(Todo, id= id)
    todo.delete()
    return redirect('/dashboard/')
from django.shortcuts import redirect, get_object_or_404
from .models import Todo

def completed(request, id):
    # Görevi veritabanından al veya 404 hatası göster
    todo = get_object_or_404(Todo, id=id)
    
    # Görevin tamamlanma durumunu tersine çevir
    todo.completed = not todo.completed
    
    # Değişikliği kaydet
    todo.save()
    
    # ToDo listesine geri dön
    return redirect('/dashboard/')  # veya 'dashboard' adlı bir URL'nizi kullanabilirsiniz




	

	
