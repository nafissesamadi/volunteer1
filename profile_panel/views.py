from pyexpat.errors import messages

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from account.models import User, Profile, PublicPlace
from .forms import EditUserModelForm, EditProfileModelForm, SchoolProfileModelForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class CompleteUserProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_profile=Profile.objects.filter(user=current_user).first()
        edit_user_form = EditUserModelForm(instance=current_user)
        edit_profile_form = EditProfileModelForm(instance=current_profile)
        context = {
            'edit_user': edit_user_form,
            'edit_profile': edit_profile_form,
            'current_user': current_user
        }
        return render(request, 'profile_panel/user_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_profile = Profile.objects.filter(user=current_user).first()
        edit_user_form = EditUserModelForm(request.POST, instance=current_user)
        edit_profile_form = EditProfileModelForm(request.POST, instance=current_profile)
        if edit_user_form.is_valid():
            edit_user_form.save()
        if edit_profile_form.is_valid():
            edit_profile_form.save()
        if current_profile.national_code is None:
            edit_profile_form.add_error('national_code', 'کد ملی اجباری است')
        if current_profile.province is None:
            edit_profile_form.add_error('province', 'انتخاب استان اجباری است')
        if current_profile.city is None:
            edit_profile_form.add_error('city', 'انتخاب شهر اجباری است')
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('/profile')
        context = {
            'edit_user': edit_user_form,
            'edit_profile': edit_profile_form,
            'current_user': current_user,
            'current_profile': current_profile
        }
        return render(request, 'profile_panel/user_profile.html', context)


class CompleteSchoolProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile=Profile.objects.filter(user_id=current_user.id).first()
        school, created=PublicPlace.objects.get_or_create(director_id=current_user.id,
                                                          province_id=profile.province_id, city_id=profile.city_id)
        school_profile_form = SchoolProfileModelForm(instance=school)
        context = {
            'school_profile': school_profile_form,
            'current_user': current_user,
            'school': school
        }
        return render(request, 'profile_panel/school_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile = Profile.objects.filter(user_id=current_user.id).first()
        school, created = PublicPlace.objects.get_or_create(director_id=current_user.id,
                                                            province_id=profile.province_id, city_id=profile.city_id)
        school_profile_form = SchoolProfileModelForm(request.POST, instance=school)
        if school_profile_form.is_valid():
            school_profile_form.save()
            if school.name is None:
                school_profile_form.add_error('name', 'لطفا نام مدرسه را وارد کنید')
            if school.type is None:
                school_profile_form.add_error('type', 'لطفا نوع مدرسه را مشخص کنید')
            if school_profile_form.is_valid():
                school_profile_form.save()
                return redirect('/profile')
        context = {
            'school_profile': school_profile_form,
            'school': school,
            'current_user': current_user
        }
        return render(request, 'profile_panel/school_profile.html', context)






def user_panel_page(request:HttpRequest):
    current_user = User.objects.filter(id=request.user.id).first()
    context = {
        'current_user': current_user
    }
    return render(request,"profile_panel/user_panel.html", context)

def user_panel_left_sidebar(request:HttpRequest):
    current_user = User.objects.filter(id=request.user.id).first()
    context = {
        'current_user': current_user
    }
    return render(request, "profile_panel/components/user_panel_left_sidebar.html", context)
