from django import forms
from django.core import validators

from account.models import User, UserType, Province,City, Profile, PublicPlace
from .models import Application, AvailableTime, WeekDay, AcceptedApplication
from django.core.exceptions import ValidationError




class CompleteApplicationModelForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = ['preferred_style', 'short_description', 'num_of_student', 'free_day_1', 'free_time_1']
        # fields='__all__'
        # exclude=['response']
        # venue = forms.ModelChoiceField(
        #     widget=forms.Select,
        #     queryset=PublicPlace.objects.all(),
        # )
        free_day_1 = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=WeekDay.objects.all(),
        )
        free_time_1 = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=AvailableTime.objects.all(),
        )
        widgets = {
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
            'free_day_1': forms.Select(attrs={
                'class': 'form-control'
            }),
            'free_time_1': forms.Select(attrs={
                'class': 'form-control'
            }),
            'preferred_style': forms.Select(attrs={
                'class': 'form-control'
            }),

            # 'venue': forms.Select(attrs={
            #     'class': 'form-control'
            # }),
            'num_of_student': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }

        labels = {
            'preferred_style': ':شیوه برگزاری',
            'free_day_1': 'روز مورد نظر',
            'free_time_1': 'زمان مورد نظر',
            # 'venue': 'مکان مورد نظر',
            'num_of_student': 'نفرات کلاس',
            'short_description': 'توضیحات',
        }

        error_messages = {
            'preferred_style': {
                'required': 'Please Enter Your preferred style'
            }
        }




class CompleteAcceptedApplicationModelForm(forms.ModelForm):
    class Meta:
        model = AcceptedApplication

        fields = ['from_date', 'to_date']
        # fields='__all__'
        # exclude=['response']

        widgets = {
            'from_date': forms.DateInput(attrs={
                'class': 'form-control',

            }),

            'to_date': forms.DateInput(attrs={
                'class': 'form-control'
            }),

        }

        labels = {
            'from_date': 'از تاریخ',
            'to_date': 'تا تاریخ',
        }
