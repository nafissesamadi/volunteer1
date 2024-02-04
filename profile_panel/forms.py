from django import forms
from django.core import validators

from account.models import User, UserType, Province,City, Profile
from django.core.exceptions import ValidationError



class EditUserModelForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'username', 'email', 'user_type']
        # fields='__all__'
        # exclude=['response']

        user_type = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=UserType.objects.all(),
        )
        widgets = {
            # 'email': forms.TextInput(attrs={
            #     'class': 'form-control'
            # }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'user_type': forms.Select(attrs={
                'class': 'form-control'
            }),

        }

        labels = {
            # 'email': 'ایمیل',
            'user_type': 'نوع کاربر',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'نام کاربری'
        }


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['national_code', 'gender','province', 'city']
        # fields='__all__'
        # exclude=['response']

        province = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=Province.objects.all(),
        )

        city = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=City.objects.all(),
        )
        widgets = {
            'national_code': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'province': forms.Select(attrs={
                'class': 'form-control'
            }),
            'city': forms.Select(attrs={
                'class': 'form-control'
            }),

        }

        labels = {
            'national_code': 'کد ملی',
            'gender': 'جنسیت',
            'province': 'استان',
            'city': 'شهر'
        }

        error_messages = {
            'national_code': {
                'required': 'Please Enter Your national code'
            }
        }


