from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField



'''class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Тема вести:', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Содержимое:', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": "5",
    }))
    is_published = forms.BooleanField(label='Донесено или нет?:', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория:', empty_label='Не забудь выбрать', widget=forms.Select({"class": "form-control"}))'''


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Твой логин, Джун:', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Удиви меня паролем:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Точно запомнил?', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    prayer = forms.CharField(label='Твоя клятва:', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Твой логин, Джун:', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Надеюсь, не забыл пароль:', widget=forms.PasswordInput(attrs={"class": "form-control"}))




class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Не должно начинаться с цифры')
        return title


class UserEmail(forms.Form):
    subject = forms.CharField(label='Тема письма создателю:', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст благодарочки:', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    captcha = CaptchaField()



