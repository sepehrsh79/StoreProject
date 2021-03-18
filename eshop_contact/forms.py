from django import forms
from django.core import validators


class CreateContactForm(forms.Form):

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class' : 'form-control'}),
        label='نام و نام خانوادگی ',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کارکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':' ایمیل خود را وارد کنید' , 'class' : 'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کارکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ' عنوان خود را وارد کنید' , 'class' : 'form-control'}),
        label='عنوان',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از   200 کارکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام خود را وارد کنید', 'class' : 'form-control','rows':'8'}),
        label='متن پیام'
    )
