from django import forms
from .models import User,UserMore

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email', 'first_name', 'last_name')

class PainelMoreForm(forms.ModelForm):
    cep = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"00.000-000"}))
    fone = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"(00) 00000-0000"}))
    class Meta:
        model = UserMore
        exclude = ["user"]

class PainelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha antiga')
    new_password = forms.CharField(widget=forms.PasswordInput(), label = 'Nova senha')

