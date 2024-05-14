from pyexpat.errors import messages

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from account.models import User, Profile, PublicPlace
from application.models import SchoolProfile, InstituteProfile, Applicant, EducationalVolunteer
from .forms import EditUserModelForm, PublicPlaceModelForm, SchoolProfileModelForm, \
    InstituteProfileModelForm, StudentProfileModelForm, EducationalVolunteerProfileModelForm, ProfileModelForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView




class CompleteSchoolProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile = Profile.objects.filter(user_id=current_user.id).first()
        school = PublicPlace.objects.filter(director_id=current_user.id).first()
        if school is None:
            school = PublicPlace.objects.create(director=current_user,
                                                province_id=profile.province_id,
                                                city_id=profile.city_id)
        school_profile, created = SchoolProfile.objects.get_or_create(school=school)
        school_form = PublicPlaceModelForm(instance=school)
        school_profile_form = SchoolProfileModelForm(instance=school_profile)
        context = {
            'school_form': school_form,
            'school_profile_form': school_profile_form,
            'current_user': current_user,
            'school': school,
            'school_pprofile' : school_profile
        }
        return render(request, 'profile_panel/school_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile = Profile.objects.filter(user_id=current_user.id).first()
        school=PublicPlace.objects.filter(director_id=current_user.id).first()
        if school is None:
            school = PublicPlace.objects.create(director=current_user,
                                                                province_id=profile.province_id,
                                                                city_id=profile.city_id)
        school_profile, created = SchoolProfile.objects.get_or_create(school=school)
        school_form = PublicPlaceModelForm(request.POST, instance=school)
        school_profile_form = SchoolProfileModelForm(request.POST, instance=school_profile)
        if school_form.is_valid():
            school_form.save()
        if school_profile_form.is_valid():
            school_profile_form.save()
        if school.name is None:
            school_form.add_error('name', 'لطفا نام مدرسه را وارد کنید')
        if school.district is None:
            school_form.add_error('district', 'لطفا منطقه یا خیابان اصلی را وارد کنید')
        if school.type is None:
            school_form.add_error('type', 'لطفا نوع آموزشگاه را مشخص کنید')
        if school_form.is_valid():
            school_form.save()
            return redirect('/profile')
        context = {
            'school_form': school_form,
            'school_profile_form': school_profile_form,
            'current_user': current_user,
            'school': school,
            'school_profile' : school_profile
        }
        return render(request, 'profile_panel/school_profile.html', context)


class CompleteInstituteProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile = Profile.objects.filter(user_id=current_user.id).first()
        institute = PublicPlace.objects.filter(director_id=current_user.id).first()
        if institute is None:
            institute = PublicPlace.objects.create(director=current_user,
                                                province_id=profile.province_id,
                                                city_id=profile.city_id)
        institute_profile, created = InstituteProfile.objects.get_or_create(institute=institute)
        institute_form = PublicPlaceModelForm(instance=institute)
        institute_profile_form = InstituteProfileModelForm(instance=institute_profile)
        context = {
            'institute_form': institute_form,
            'institute_profile_form': institute_profile_form,
            'current_user': current_user,
            'institute': institute,
            'institute_profile' : institute_profile
        }
        return render(request, 'profile_panel/institute_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        profile = Profile.objects.filter(user_id=current_user.id).first()
        institute=PublicPlace.objects.filter(director_id=current_user.id).first()
        if institute is None:
            institute = PublicPlace.objects.create(director=current_user,
                                                                province_id=profile.province_id,
                                                                city_id=profile.city_id)
        institute_profile, created = InstituteProfile.objects.get_or_create(institute=institute)
        institute_form = PublicPlaceModelForm(request.POST, instance=institute)
        institute_profile_form = InstituteProfileModelForm(request.POST, instance=institute_profile)
        if institute_form.is_valid():
            institute_form.save()
        if institute_profile_form.is_valid():
            institute_profile_form.save()
        if institute.name is None:
            institute_form.add_error('name', 'لطفا نام مکان آموزشی را وارد کنید')
        if institute.district is None:
            institute_form.add_error('district', 'لطفا منطقه یا خیابان اصلی را وارد کنید')
        if institute.type is None:
            institute_form.add_error('type', 'لطفا نوع آموزشگاه را مشخص کنید')
        if institute_form.is_valid():
            institute_form.save()
            return redirect('/profile')
        context = {
            'institute_form': institute_form,
            'institute_profile_form': institute_profile_form,
            'current_user': current_user,
            'institute': institute,
            'institute_profile' : institute_profile
        }
        return render(request, 'profile_panel/institute_profile.html', context)


class StudentProfilrModelForm(object):
    pass


class CompleteStudentProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        student, created = Applicant.objects.get_or_create(user=current_user)
        student_form = StudentProfileModelForm(instance=student, request=request)
        context = {
            'student_form': student_form,
            'current_user': current_user,
        }
        return render(request, 'profile_panel/student_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        student, created = Applicant.objects.get_or_create(user=current_user)
        student_form = StudentProfileModelForm(request.POST, instance=student, request=request)
        if student_form.is_valid():
            student_form.save()
            return redirect('/profile')
        context = {
            'student_form': student_form,
            'current_user': current_user,
        }
        return render(request, 'profile_panel/student_profile.html', context)



class CompleteVolunteerProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        educational_volunteer, created = EducationalVolunteer.objects.get_or_create(user=current_user)
        educational_volunteer_form = EducationalVolunteerProfileModelForm(instance=educational_volunteer)
        context = {
            'volunteer_form': educational_volunteer_form,
            'current_user': current_user,
        }
        return render(request, 'profile_panel/volunteer_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        educational_volunteer, created = EducationalVolunteer.objects.get_or_create(user=current_user)
        educational_volunteer_form = EducationalVolunteerProfileModelForm(request.POST, instance=educational_volunteer)
        if educational_volunteer_form.is_valid():
            educational_volunteer_form.save()
            return redirect('/profile')
        context = {
            'volunteer_form': educational_volunteer_form,
            'current_user': current_user,
        }
        return render(request, 'profile_panel/volunteer_profile.html', context)

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


class CompleteUserProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_profile=Profile.objects.filter(user=current_user).first()
        edit_user_form = EditUserModelForm(instance=current_user)
        edit_profile_form = ProfileModelForm(instance=current_profile)
        context = {
            'form': edit_profile_form,
            'edit_user': edit_user_form,
            'current_user': current_user
        }
        return render(request, 'profile_panel/user_profile.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_profile = Profile.objects.filter(user=current_user).first()
        edit_user_form = EditUserModelForm(request.POST, instance=current_user)
        edit_profile_form = ProfileModelForm(request.POST, instance=current_profile)
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
            'form': edit_profile_form,
            'current_user': current_user,
            'edit_user': edit_user_form,
            'current_profile': current_profile
        }
        return render(request, 'profile_panel/user_profile.html', context)