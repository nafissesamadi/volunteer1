from django import forms
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator


from account.models import User, UserType, Province, City, Profile, PublicPlace, PublicPlaceType
from django.core.exceptions import ValidationError

from application.models import SchoolProfile, EducationalLevel, InstituteProfile, AvailableTime, WeekDay, Applicant, Grade, Major


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
    


class PublicPlaceModelForm(forms.ModelForm):
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
            'address': 'آدرس ',
            'type': 'نوع',
        }

        error_messages = {
            'name': {
                'required': ' لطفا نام مدرسه وارد کنید'
            }
        }


class SchoolProfileModelForm(forms.ModelForm):
    class Meta:
        model = SchoolProfile

        fields = ['school_level', 'educational_district','short_description']

        type = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=EducationalLevel.objects.all(),

        )

        educational_district = forms.CharField(
            validators=[
                validators.MaxLengthValidator(10),
            ]
        )

        widgets = {

            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'بیوگرفافی مدرسه',
                'rows': 5,
            }),
            'educational_district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ناحیه آموزشی '
            }),
            'school_level': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'مقطع تحصیلی'
            }),
        }

        labels = {
            'educational_district': 'ناحیه آموزشی',
            'short_description': 'بیوگرافی مدرسه',
            'school_level': 'مقطع تحصیلی',

        }


class InstituteProfileModelForm(forms.ModelForm):
    class Meta:
        model = InstituteProfile

        fields = ['available_time', 'available_day','short_description']

        available_time = forms.ModelMultipleChoiceField(
            queryset=AvailableTime.objects.all(),

        )
        available_day = forms.ModelMultipleChoiceField(
            queryset=WeekDay.objects.all(),

        )

        widgets = {

            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'بیوگرفافی موسسه',
                'rows': 5,
            }),
            'available_time': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'روز های موجود '
            }),
            'available_day': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'زملن های موجود'
            }),
        }

        labels = {
            'available_time': 'زمان های موجود',
            'available_day': 'روز های موجود',
            'short_description': 'بیوگرافی مدرسه',

        }

class StudentProfileModelForm(forms.ModelForm):
    class Meta:
        model = Applicant



        fields = ['school', 'grade', 'major', 'gpa', 'is_worker','is_student', 'special_condition']

        # school = forms.ModelChoiceField(
        #     widget=forms.Select,
        #     queryset=PublicPlace.objects.filter()
        # )
        grade = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=Grade.objects.all(),
        )
        major = forms.ModelChoiceField(
            widget=forms.Select,
            queryset=Major.objects.all(),
        )

        gpa = forms.DecimalField(
            validators=[MinValueValidator(1), MaxValueValidator(20)]
        )

        widgets = {

            'special_condition': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'بیوگرافی دانش آموز',
                'rows': 5,
            }),
            'is_worker': forms.CheckboxInput(attrs={
                'placeholder': 'کار می کنم '
            }),
            'is_student': forms.CheckboxInput(attrs={

                'placeholder': 'مدرسه می روم '
            }),
            'grade': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'پایه تحصیلی'
            }),
            'major': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'رشته تحصیلی'
            }),
            'school': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'مدرسه'
            }),
            'gpa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'معدل',
            }),
        }

        labels = {
            'grade': 'پایه تحصیلی',
            'major': 'رشته تحصیلی',
            'school': 'مدرسه',
            'special_condition': 'بیوگرافی',
            'gpa': 'معدل',
            'is_worker': 'کار می کنم',
            'is_student': 'مدرسه نمی روم',

        }



    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(StudentProfileModelForm, self).__init__(*args, **kwargs)
        current_user=self.request.user
        profile=Profile.objects.filter(user=current_user).first()
        self.fields["school"].queryset = PublicPlace.objects.filter(province_id=profile.province_id,
                                                                    city_id=profile.city_id,
                                                                    type__title__contains="مدرسه")





