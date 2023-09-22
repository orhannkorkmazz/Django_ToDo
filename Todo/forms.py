from django import forms
from .models import Todo

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=50,label="Parolanızı Doğrulayınız",widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password!=confirm :
            raise forms.ValidationError("Girdiğiniz parolalar uyuşmuyor,lütfen kontrol ediniz")
        else:
            values={
                "username":username,
                "password":password
            }
        return values
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','due_date']
