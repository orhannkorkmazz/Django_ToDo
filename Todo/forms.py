from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=50,label="Parolanızı Doğrulayınız",widget=forms.PasswordInput)