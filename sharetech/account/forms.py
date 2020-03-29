from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email', 'first_name', 'last_name')
        
class PainelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha antiga')
    new_password = forms.CharField(widget=forms.PasswordInput(), label = 'Nova senha')

