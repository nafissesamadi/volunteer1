from django import forms
from django.core import validators

from account.models import User, UserType, Province,City, Profile
from .models import Application, AvailableTime,ClassVenue, WeekDay
from django.core.exceptions import ValidationError




class CompleteApplicationModelForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = ['preferred_style', 'short_description','free_day_1','free_time_1', 'demandend_venue', 'num_of_student']
        # fields='__all__'
        # exclude=['response']


        demanded_venue = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=ClassVenue.objects.all(),
        )
        free_day_1 = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=WeekDay.objects.all(),
        )
        free_time_1 = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=AvailableTime.objects.all(),
        )
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'free_day_1': forms.Select(attrs={
                'class': 'form-check-inline'
            }),
            'free_time_1': forms.Select(attrs={
                'class': 'form-check-inline'
            }),
            'preferred_style': forms.RadioSelect(attrs={
                'class': 'form-check-inline'
            }),

            'demandend_venue': forms.Select(attrs={
                'class': 'form-control'
            }),
            'num_of_student': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }

        labels = {
            # 'preferred_style': ':شیوه برگزاری',
            'demandend_time': 'زمان مورد نظر',
            'demandend_venue': 'مکان مورد نظر',
            'short_description': 'توضیحات'
        }

        error_messages = {
            'preferred_style': {
                'required': 'Please Enter Your preferred style'
            }
        }