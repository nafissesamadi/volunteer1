from django import forms
from django.core import validators

from account.models import User, UserType, Province, City, Profile, PublicPlace, PublicPlaceType
from django.core.exceptions import ValidationError



class EditUserModelForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name']
        # fields='__all__'
        # exclude=['response']

        # user_type = forms.ModelChoiceField(
        #     widget=forms.Select,
        #     queryset=UserType.objects.all(),
        # )
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
            # 'username': forms.TextInput(attrs={
            #     'class': 'form-control'
            # }),
            # 'user_type': forms.Select(attrs={
            #     'class': 'form-control'
            # }),

        }

        labels = {
            # 'email': 'ایمیل',
            # 'user_type': 'نوع کاربر',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            # 'username': 'نام کاربری'
        }


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['national_code', 'gender','province', 'city', 'birth_date','nationality' ]
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

        national_code = forms.CharField(
                widget=forms.CharField(required=True),
                validators=[
                    validators.MaxLengthValidator(10),
                ]
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
            'nationality': forms.Select(attrs={
                'class': 'form-control'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
            }),

        }

        labels = {
            'national_code': 'کد ملی',
            'gender': 'جنسیت',
            'province': 'استان',
            'city': 'شهر',
            'birth_date': 'تاریخ تولد',
            'nationality': 'ملیت',
        }

        # error_messages = {
        #     'national_code': {
        #         'required': 'کد ملی اجباری می باشد. لطفا وارد کنید'
        #     }
        # }


class SchoolProfileModelForm(forms.ModelForm):
    class Meta:
        model = PublicPlace

        fields = ['name', 'type','district', 'address']

        type = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=PublicPlaceType.objects.all(),
        )
        name = forms.CharField(required=True)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام مدرسه'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'خیابان اصلی'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'خیابان فرعی / کوچه / پلاک '
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'نوع آموزشگاه'
            }),
        }

        labels = {
            'name': 'نام مدرسه',
            'district': 'آدرس',
            'address': 'آدرس',
            'type': 'نوع',

        }

        error_messages = {
            'name': {
                'required': ' لطفا نام مدرسه وارد کنید'
            }
        }




