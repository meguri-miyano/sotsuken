from django import forms
from .models import Menudata

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Menudata
        fields = ('menuname',)
        labels={
            'menuname':'メニュー名',
        }
