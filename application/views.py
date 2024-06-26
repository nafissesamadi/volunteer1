from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from account.models import User, PublicPlaceType, Province, City, Profile
from .models import Application, Course, EducationalLevel, Major, Grade, AvailableTime, PublicPlace, AcceptedApplication
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from application.forms import CompleteApplicationModelForm, CompleteAcceptedApplicationModelForm


# region Application_List
# Create your views here.
# def application_list(request):
#     applications = Application.objects.all().order_by('registered_date')
#     return render(request, 'application/application_list.html', {'applications': applications})


# class ApplicationListView(TemplateView):
#     template_name = 'application/application_list.html'
#     def get_context_data(self, **kwargs):
#         applications=Application.objects.all().order_by('rating')
#         context=super(ApplicationListView,self).get_context_data()
#         context['applications'] = applications
#         return context

class ApplicationListView(ListView):
    template_name = 'application/application_list.html'
    model = Application
    context_object_name = 'applications'
    # ordering = ['code']
    paginate_by = 10

    def get_queryset(self):
        query = super(ApplicationListView, self).get_queryset()
        data = query.filter(is_active=True, is_accepted=False)
        return data



# endregion

# region Application_detail

# def application_detail(request, application_id):
#     application = get_object_or_404(Application, pk=application_id)
#     return render(request, 'application/application_detail.html', {'application': application})

# class ApplicationDetailView(TemplateView):
#     template_name = 'application/application_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ApplicationDetailView, self).get_context_data()
#         application_id = kwargs['application_id']
#         application = get_object_or_404(Application, pk=application_id)
#         context['application'] = application
#         return context

class ApplicationDetailView(DetailView):
    template_name = 'application/application_detail.html'
    model = Application

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_application = self.object
        request = self.request
        favorite_application_id = request.session.get("application_favorites")
        context['is_favorite'] = favorite_application_id == str(loaded_application.id)
        current_user = self.request.user
        context['current_user'] = current_user
        return context


# endregion

class AddMyFavoriteApplication(View):
    def post(self, request):
        application_id = request.POST["application_id"]
        application = Application.objects.get(pk=application_id)
        request.session["application_favorites"] = application_id
        return redirect(application.get_absolute_url())


# region Course_list
class CoursesListView(ListView):
    model = Course
    paginate_by = 8
    ordering = ['-code']
    template_name = 'application/course_page.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CoursesListView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_queryset(self):
        query = super(CoursesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query1 = query.filter(grade__url_title__iexact=category_name)
        return query1

    def get_queryset(self):
        query = super(CoursesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        category_major = self.kwargs.get('major')
        if category_name is not None:
            query = query.filter(grade__url_title__iexact=category_name, major__url_title__iexact=category_major)
        return query


def course_categories_component(request: HttpRequest):
    course_edu_level = EducationalLevel.objects.all()
    context = {
        'course_edu_level': course_edu_level,
    }
    return render(request, 'application/components/course_categories_component.html', context)


def course_categories_major(request: HttpRequest):
    course_major = Major.objects.filter(is_active=True)
    course_grade = Grade.objects.filter(edu_level__url_title="senior", is_active=True)
    context = {
        'course_grade': course_grade,
        'course_major': course_major,
    }
    return render(request, 'application/components/course_categories_major.html', context)


# endregion

# region Venue_List
class PublicPlaceDetailView(DetailView):
    template_name = 'application/publicplace_detail.html'
    model = PublicPlace

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super(PublicPlaceDetailView,self).get_context_data()
        context["schools"]=PublicPlace.objects.filter(type__title__contains="مدرسه")
        context['app'] = self.kwargs.get('app')
        current_user = self.request.user
        inactive_app =Application.objects.filter(applicant_id=current_user.id, is_active=False).first()
        if inactive_app is not None:
            context['inactive_app_num']=inactive_app.id
        return context


class PublicPlaceListView(ListView):
    template_name = 'application/publicplace_list.html'
    model = PublicPlace
    context_object_name = 'publicplaces'
    # ordering = ['code']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublicPlaceListView, self).get_context_data()
        context['app'] = self.kwargs.get('app')
        return context

    def get_queryset(self):
        base_query = super(PublicPlaceListView, self).get_queryset()
        current_user = self.request.user
        profile = Profile.objects.filter(user_id=current_user.id).first()
        data = base_query.filter(province_id=profile.province_id, city_id=profile.city_id)
        return data



def venues_by_type(request: HttpRequest):
    venue = PublicPlaceType.objects.all()
    context = {
        'venue': venue,
    }
    return render(request, 'application/components/publicplace_by_type.html', context)


# endregion


def add_course_to_application(request: HttpRequest):
    course_id = request.GET.get('course_id')
    applicant = User.objects.filter(id=request.user.id).first()
    school = PublicPlace.objects.filter(applicant__user_id=request.user.id).first()
    if applicant.is_authenticated:
        if applicant.user_type_id == 3 or applicant.user_type_id == 4:
            demanded_course = Course.objects.filter(id=course_id).first()
            if demanded_course is not None:
                duplicate_application = Application.objects.filter(applicant_id=applicant.id, is_active=True,
                                                                       demanded_course_id=demanded_course.id).first()
                if duplicate_application is None:
                    previous_application = Application.objects.filter(applicant_id=applicant.id, is_active=False,
                                                                      is_accepted=False).first()
                    if previous_application is not None:
                        previous_application.delete()
                    application = Application.objects.create(applicant_id=applicant.id,
                                                             demanded_course_id=demanded_course.id)
                    if school is not None:
                        application.venue_id = school.id
                    else:
                        application.venue = None
                    application.save()
                    return JsonResponse({
                        'status': 'success',
                        'text': 'درس مورد نظر با موفقیت به فرم تقاضا اضافه شد',
                        'confirm_button_text': 'باشه ممنونم',
                        'icon': 'success'
                    })
                else:
                    return JsonResponse({
                        'status': 'duplicate_course',
                        'text': 'شما قبلا این درس را درخواست داده اید',
                        'confirm_button_text': 'مرسی از شما',
                        'icon': 'warning'
                    })
            else:
                return JsonResponse({
                    'status': 'not_found',
                    'text': 'درس مورد نظر یافت نشد',
                    'confirm_button_text': 'مرسییییی',
                    'icon': 'error'
                })
        else:
            return JsonResponse({
                'status': 'not_eligible',
                'text': 'فقط دانش آموزان و مدیران می توانند تفاضای درس بدهند',
                'confirm_button_text': 'باشه ممنون',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای انتخاب درس ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })


class CompleteApplication(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_application = Application.objects.filter(applicant=current_user, is_active=False,
                                                         is_accepted=False).first()
        application_form = CompleteApplicationModelForm(instance=current_application)
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/complete_application.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        current_application = Application.objects.filter(applicant=current_user, is_active=False).first()
        # current_application.venue_id = school.id
        if current_application is not None:
            application_form = CompleteApplicationModelForm(request.POST, instance=current_application)
            if application_form.is_valid():
                if current_application.venue is not None:
                    current_application.preferred_style = 'FTF'
                else:
                    current_application.preferred_style = 'V'
                current_application.is_active = True
                application_form.save()
                return redirect(reverse('application_list'))
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/complete_application.html', context)


def remove_venue(request: HttpRequest):
    venue_id = request.GET.get('venue_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, is_active=False,
                                                         venue_id=venue_id).first()
        current_application.venue = None
        current_application.save()
    else:
        return JsonResponse({'status': 'Not_Auth'})


def remove_active_application(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, id=application_id).first()
        current_application.delete()
    else:
        return JsonResponse({'status': 'Not_Auth'})


def remove_inactive_application(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, id=application_id).first()
        current_application.delete()
    else:
        return JsonResponse({'status': 'Not_Auth'})


def remove_app_from_volunteer(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, id=application_id).first()
        accepted_application = AcceptedApplication.objects.filter(application_id=application_id)
        current_application.is_accepted = False
        current_application.save()
        accepted_application.delete()

    else:
        return JsonResponse({'status': 'Not_Auth'})

def remove_accepted_application_by_volunteer(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(acceptedapplication__edu_volunteer_id=applicant.id, id=application_id).first()
        accepted_application = AcceptedApplication.objects.filter(application_id=application_id)
        current_application.is_accepted = False
        current_application.save()
        accepted_application.delete()

    else:
        return JsonResponse({'status': 'Not_Auth'})


def remove_course(request: HttpRequest):
    course_id = request.GET.get('course_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, is_active=False).first()
        current_application.delete()
    else:
        return JsonResponse({'status': 'Not_Auth'})


def remove_venue_in_edit_mode(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        current_application = Application.objects.filter(applicant_id=applicant.id, id=application_id).first()
        current_application.venue = None
        current_application.save()
    else:
        return JsonResponse({'status': 'Not_Auth'})


def accept_application(request: HttpRequest):
    application_id = request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        if applicant.user_type_id == 2:
            previous_accepted_application = AcceptedApplication.objects.filter(edu_volunteer_id=applicant.id,
                                                                               is_active=False).first()
            if previous_accepted_application is not None:
                previous_accepted_application.delete()
                previous_application = Application.objects.filter(
                    id=previous_accepted_application.application_id).first()
                previous_application.is_accepted = False
                previous_application.save()
            application = Application.objects.filter(id=application_id).first()
            if application is not None:
                application.is_accepted = True
                application.save()
                accepted_application = AcceptedApplication.objects.create(application_id=application.id,
                                                                          edu_volunteer_id=applicant.id)
                accepted_application.save()
                return JsonResponse({
                    'status': 'success',
                    'text': 'تقاضای مورد نظر با موفقیت اضافه شد',
                    'confirm_button_text': 'باشه ممنونم',
                    'icon': 'success'})
            else:
                return JsonResponse({
                    'status': 'not_found',
                    'text': 'تقاضای مورد نظر یافت نشد',
                    'confirm_button_text': 'مرسییییی',
                    'icon': 'error'})
        else:
            return JsonResponse({
                'status': 'not_eligible',
                'text': 'فقط داوطلبان می توانند تفاضای درس بدهند',
                'confirm_button_text': 'باشه ممنون',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای انتخاب درس ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'})


class CompleteAcceptedApplication(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        accepted_application = AcceptedApplication.objects.filter(edu_volunteer_id=current_user.id,
                                                                  is_active=False).first()
        application = Application.objects.filter(id=accepted_application.application_id).first()
        accepted_application_form = CompleteAcceptedApplicationModelForm(instance=accepted_application)
        context = {
            'accepted_application': accepted_application,
            'accepted_application_form': accepted_application_form,
            'current_user': current_user,
            'application': application
        }
        return render(request, 'application/accept_application.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        accepted_application = AcceptedApplication.objects.filter(edu_volunteer_id=current_user.id,
                                                                  is_active=False).first()
        application = Application.objects.filter(id=accepted_application.application_id).first()
        if accepted_application is not None:
            accepted_application_form = CompleteAcceptedApplicationModelForm(request.POST,
                                                                             instance=accepted_application)
            if accepted_application_form.is_valid():
                accepted_application.is_active = True
                accepted_application_form.save()
                return redirect(reverse('application_list'))
        context = {
            'accepted_application': accepted_application,
            'accepted_application_form': accepted_application_form,
            'current_user': current_user,
            'application': application
        }
        return render(request, 'application/accept_application.html', context)


class UserApplicationListView(ListView):
    template_name = 'application/user_application_list.html'
    model = Application
    context_object_name = 'applications'
    ordering = ['registered_date']
    paginate_by = 9

    def get_queryset(self):
        base_query = super(UserApplicationListView, self).get_queryset()
        current_user = self.request.user
        application = base_query.filter(applicant_id=current_user.id)
        return application


class VolunteerclassListView(ListView):
    template_name = 'application/volunteer_class_list.html'
    model = Application
    context_object_name = 'applications'
    ordering = ['registered_date']
    paginate_by = 9

    def get_queryset(self):
        base_query = super(VolunteerclassListView, self).get_queryset()
        current_user = self.request.user
        application = base_query.filter(acceptedapplication__edu_volunteer_id=current_user.id)
        # application=Application.objects.filter(acceptedapplication__edu_volunteer=current_user).all()
        return application


class EditActiveApplication(View):
    def get(self, request: HttpRequest, application_id):
        current_user = User.objects.filter(id=request.user.id).first()
        # application_id=request.GET.get('application_id')
        current_application = get_object_or_404(Application, applicant=current_user, id=application_id)
        application_form = CompleteApplicationModelForm(instance=current_application)
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/edit_active_application.html', context)

    def post(self, request: HttpRequest, application_id):
        current_user = User.objects.filter(id=request.user.id).first()
        # application_id = request.GET.get('application_id')
        current_application = get_object_or_404(Application, applicant=current_user, id=application_id)
        # current_application.venue_id = school.id
        if current_application is not None:
            application_form = CompleteApplicationModelForm(request.POST, instance=current_application)
            if application_form.is_valid():
                if current_application.venue is not None:
                    current_application.preferred_style = 'FTF'
                else:
                    current_application.preferred_style = 'V'
                current_application.is_active = True
                application_form.save()
                return redirect(reverse('application_list'))
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/edit_active_application.html', context)


def add_venue_to_application(request: HttpRequest):
    venue_id = request.GET.get('venue_id')
    app_number=request.GET.get('application_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        if applicant.user_type_id == 3 or applicant.user_type_id == 4:
            venue = PublicPlace.objects.filter(id=venue_id).first()
            if venue is not None:
                application = Application.objects.filter(id=app_number).first()
                application.venue_id = venue_id
                application.save()
            else:
                return JsonResponse({
                    'status': 'not_found'
                })
        return JsonResponse({
            'status': 'not_eligible'
        })
    return JsonResponse({
        'status': 'not_auth'
    })




class OngoingApplicationListView(ListView):
    template_name = 'application/ongoing_application_list.html'
    model = Application
    context_object_name = 'applications'
    ordering = ['registered_date']
    paginate_by = 8

    def get_queryset(self):
        query = super(OngoingApplicationListView, self).get_queryset()
        applicant = self.request.user
        profile = Profile.objects.filter(user_id=applicant.id).first()
        application = query.filter(is_active=True,is_accepted=True,
                                   acceptedapplication__is_active=True,
                                   acceptedapplication__is_finished=False)
        return application
