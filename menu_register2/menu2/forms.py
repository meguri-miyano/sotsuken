from django import forms
from .models import Menudata
from .import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Menudata
        fields = ('menuname','')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['menuname'].widget.attrs['class'] = 'form-cntrol col-9'
        self.fields['menuname'].widget.attrs['placeholder'] = 'メニュー名を入力してください。'
    
    


