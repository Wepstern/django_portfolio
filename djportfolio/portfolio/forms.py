from django import forms
from .models import User


class MyForm(forms.MyForm):
    class Meta:
        model = User
        fields = ['sex', ]
