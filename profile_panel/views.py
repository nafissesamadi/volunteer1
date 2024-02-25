from pyexpat.errors import messages

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from account.models import User, Profile
from .forms import EditUserModelForm, EditProfileModelForm
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
            return redirect('/profile')
        context = {
            'edit_user': edit_user_form,
            'edit_profile': edit_profile_form,
            'current_user': current_user,
            'current_profile': current_profile
        }
        return render(request, 'profile_panel/user_profile.html', context)



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
