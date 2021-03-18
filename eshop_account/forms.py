from django import forms
from django.contrib.auth.models import User
from django.core import validators

class EditUserForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام  خود را وارد کنید', 'class' : 'form-control'}),
                               label='نام')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید' , 'class' : 'form-control'}),
                                 label='نام خانوادگی')

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
                               label='نام کاربری')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' رمز عبور خود را وارد کنید'}),
                               label='رمز عبور')

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        is_exist_user = User.objects.filter(username = user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError('نام کاربری یافت نشد')
        return user_name


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
                               label='نام کاربری')

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید'}),
                               label='ایمیل',
                               validators = [validators.MaxLengthValidator(limit_value=20,message='تعداد کارکتر های ایمیل باید کمتر از 20 تا باشد' ),
                                            validators.MinLengthValidator(8,'تعتداد کارکتر های ایمیل باید بیشتر از 8 تا باشد ')
                                             ])


    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' رمز عبور خود را وارد کنید'}),
                               label='رمز عبور')

    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' رمز عبور خود را دوبارع وارد کنید'}),
                               label='تکرار رمز عبور')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_user_by_email = User.objects.filter(email=email).exists()
        if is_exist_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های غبور مغایرت دارند')
        return password

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        is_exist_user_by_username = User.objects.filter(username = user_name).exists()
        if is_exist_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت شده است')
        return user_name