from django import forms
from .models import Todo

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=50,label="Parolanızı Doğrulayınız",widget=forms.PasswordInput)
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','due_date']
