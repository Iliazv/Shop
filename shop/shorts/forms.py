from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import Select
from captcha.fields import CaptchaField
from .models import Comment


class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    password1 = forms.CharField(max_length=200, help_text='Required')
    password2 = None
    captcha = CaptchaField()
    class Meta:  
        model = get_user_model()
        fields = ('email', 'password1', 'captcha')


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('name', 'score', 'delivery', 'material', 'print', 'text', 'captcha')

        labels = {
            'name': 'Ваше имя',
            'score': 'Ваша оценка',
            'delivery': 'Доставка',
            'material': 'Материал',
            'print': 'Принт',
            'text': 'Текст комментария',
        }
        widgets = {
            'score': Select(attrs={
                'class': "form-control1", 
                'style': 'width: 160px; height:38px ;border: 1px solid rgba(128, 128, 128, 0.5); border-radius: 4px; padding: 0 7px; font-size: 14px',
                'placeholder': 'Email'
                }),
            'delivery': Select(attrs={
                'class': "form-control1", 
                'style': 'border: 1px solid rgba(128, 128, 128, 0.5); border-radius: 4px; padding: 0 7px; font-size: 14px',
                'placeholder': 'Email'
                }),
            'material': Select(attrs={
                'class': "form-control1", 
                'style': 'border: 1px solid rgba(128, 128, 128, 0.5); border-radius: 4px; padding: 0 7px; font-size: 14px',
                'placeholder': 'Email'
                }),
            'print': Select(attrs={
                'class': "form-control", 
                'style': 'border: 1px solid rgba(128, 128, 128, 0.5); border-radius: 4px; padding: 0 7px; font-size: 14px',
                'placeholder': 'Email'
                })
        }