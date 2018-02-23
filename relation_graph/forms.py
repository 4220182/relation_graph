from django import forms

class LoginForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea) 