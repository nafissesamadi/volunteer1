from django import forms
from django.core import validators

from account.models import User, UserType
from django.core.exceptions import ValidationError


# class RegisterModelForm(forms.ModelForm):
#     class Meta:
#         model = User
#
#         fields = ['email', 'mobile','password', 'user_type']
#         # fields='__all__'
#         # exclude=['response']
#
#         user_type = forms.ModelChoiceField(
#             widget=forms.Select,
#             queryset=UserType.objects.all(),
#         )
#         widgets = {
#             'email': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'mobile': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'password': forms.TextInput(attrs={
#                 'class': 'form-control',
#             })
#         }
#
#         labels = {
#             'email': 'ایمیل',
#             'mobile': 'موبایل',
#             'user_type': 'نوع کاربر',
#             'password': 'رمز عبور'
#         }
#
#         error_messages = {
#             'mobile': {
#                 'required': 'Please Enter Your mobile'
#             }
#         }
#         confirm_password=forms.CharField(
#             label= 'تکرار کلمه عبور',
#             widget=forms.PasswordInput
#         )


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'confirm_password'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    mobile = forms.CharField(
        label='موبایل',
        required=False,
        error_messages={
            'max_length': 'شماره موبایل معتبر نیست '
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mobile'}),
        validators=[
            validators.MaxLengthValidator(11),
        ]
    )
    user_type = forms.ModelChoiceField(
        label="نوع کاربر",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'user_type'
        }), queryset=UserType.objects.all())

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError("مغایرت کلمه عبور و تکرار آن")


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class FrogetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator])



class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'password'}),
        validators=[
            validators.MaxLengthValidator(100),])
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'confirm_password'}),
        validators=[
            validators.MaxLengthValidator(100),])

