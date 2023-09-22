from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm ,LoginForm,TodoForm
from .models import Todo
from django.utils import timezone
from datetime import datetime, timedelta
from datetime import date
from django.contrib.auth.decorators import login_required
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
    if request.method=="POST":
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
        form=RegisterForm()
    return render(request,"register.html",{"form":form})


@login_required
def dashboard(request):
    filter_option = request.GET.get('filter', 'all')
    sort_option = request.GET.get('sort', 'created_date')

    todos = Todo.objects.filter(author=request.user)

   # Tarih sınırını hesaplayın: Bugünün sonu (23:59:59)
    today_end = datetime.combine(date.today(), datetime.min.time()) + timedelta(days=1) - timedelta(seconds=1)
    # Todo listesini filtreleme işlemi
    if filter_option == 'completed':
        todos = todos.filter(completed=True)
    elif filter_option == 'incomplete':
        todos = todos.filter(completed=False)
    elif filter_option == 'upcoming':
        todos = todos.filter(due_date__gte=today_end )

    # Sıralama işlemi
    if sort_option == 'created_date':
        todos = todos.order_by('created_date')
    elif sort_option == 'due_date':
        todos = todos.order_by('due_date')
    no_todos_message = None

    if not todos.exists():
        no_todos_message = "Seçilen öğe ile ilgili gösterilecek bilgi yok"
    today = date.today()
    return render(request, 'dashboard.html', {'todos': todos, 'filter_option': filter_option, 'sort_option': sort_option, "today": today, "no_todos_message": no_todos_message})

@login_required
def addtodo(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        todos=form.save(commit=False)#sadece form.save() yaparak kayıt işlemi gerçekleşebilir fakat bu formdan alınan bilgide yazar bilgisi olduğu için ve biz makalede sadece başlık ve içerik bilgisi istediğimizi için hata ile karşılaşırız 
        todos.author=request.user
        todos.save()
        return redirect("/dashboard/")
    return render(request,"addtodo.html",{"form":form} )
@login_required
def deletetodo(request,id):
    todo = get_object_or_404(Todo, id= id)
    todo.delete()
    return redirect('/dashboard/')
def completed(request, id):
    # Görevi veritabanından al veya 404 hatası göster
    todo = get_object_or_404(Todo, id=id)
    
    # Görevin tamamlanma durumunu tersine çevir
    todo.completed = not todo.completed
    
    # Değişikliği kaydet
    todo.save()
    
    # ToDo listesine geri dön
    return redirect('/dashboard/')  # veya 'dashboard' adlı bir URL'nizi kullanabilirsiniz


@login_required
def editTodo(request,id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')  # Güncellendikten sonra listeye geri dön
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'editTodo.html', {'form': form, 'todo': todo})





	

	
