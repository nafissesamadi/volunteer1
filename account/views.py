from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account.models import User
from django.contrib.auth import get_user_model, login, logout
from django.http import Http404, HttpRequest
from django.views.generic import CreateView
from account.forms import RegisterForm, LoginForm, FrogetPasswordForm, ResetPasswordForm
from django.utils.crypto import get_random_string
from utils.email_service import send_email
from django.views.generic import TemplateView

# from account.forms import RegisterModelForm

# Create your views here.

# class RegisterCreateView(CreateView):
#     form_class = RegisterModelForm
#     template_name = 'account/register.html'
#     success_url = '/register/'


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'account/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_mobile = register_form.cleaned_data.get('mobile')
            user_type = register_form.cleaned_data.get('user_type')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    mobile=user_mobile,
                    user_type=user_type,
                    is_active=True,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # send email active code
                # send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('login_page'))
            context = {
                'register_form': register_form}
            return render(request, 'account/register.html', context)
        context = {'register_form': register_form}
        return render(request, 'account/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('user_panel_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'account/login.html', context)

class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo: show "your account was activated" message to user
                pass
        raise Http404

class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = FrogetPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account/forget_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = FrogetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('login_page'))

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'account/forget_password.html', context)

class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_pass_form = ResetPasswordForm()
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user}
        return render(request, 'account/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))


