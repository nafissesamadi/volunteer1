from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from account.models import User
from .models import Application, Course, EducationalLevel, Major, Grade, AvailableTime, PublicPlace
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from application.forms import CompleteApplicationModelForm


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
    ordering = ['registered_date']
    paginate_by = 9
    # def get_queryset(self):
    #     base_query=super(ApplicationListView,self).get_queryset()
    #     data=base_query.filter(is_active=True)
    #     return data


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
    paginate_by = 10
    ordering = ['-code']
    template_name = 'application/course_page.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CoursesListView, self).get_context_data(*args, **kwargs)
    #     return context

    def get_queryset(self):
        query = super(CoursesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(grade__url_title__iexact=category_name)
        return query

    def get_queryset(self):
        query = super(CoursesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        category_major = self.kwargs.get('major')
        if category_name is not None:
            query = query.filter(grade__url_title__iexact=category_name, major__url_title__iexact=category_major)
        return query

# endregion

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


# class CompleteApplication(View):
#     def get(self, request: HttpRequest):
#         course_id = request.GET.get('course_id')
#         applicant = User.objects.filter(id=request.user.id).first()
#         demanded_course = Course.objects.filter(id=course_id).first()
#         if applicant.is_authenticated:
#             if applicant.user_type_id == 1 or applicant.user_type_id == 2:
#                 if demanded_course is not None:
#                     filtered_application = Application.objects.filter(applicant_id=applicant.id,
#                                                                       demanded_course_id=demanded_course.id).first()
#                     if filtered_application is None:
#                         current_application = Application.objects.create(applicant_id=applicant.id, demanded_course_id=course_id)
#                     else:
#                         return JsonResponse({'status': 'Already Regisred'})
#                 else:
#                     return JsonResponse({'status': 'Not Found'})
#             else:
#                 return JsonResponse({'status': 'Not eligible User_type'})
#         else:
#             return JsonResponse({'status': 'Not Auth'})
#         application = Application.objects.filter(applicant_id=applicant.id, demanded_course=demanded_course).first()
#         context = { 'application' : application }
#         return render(request, 'application/complete_application.html', context)
#     def post(self, request: HttpRequest):
#         course_id = request.GET.get('course_id')
#         applicant = User.objects.filter(id=request.user.id).first()
#         demanded_course = Course.objects.filter(id=course_id).first()
#         filtered_application = Application.objects.filter(applicant_id=applicant.id,
#                                                           demanded_course_id=demanded_course.id).first()
#         if applicant.is_authenticated:
#             if applicant.user_type_id == 1 or applicant.user_type_id == 2:
#                 if demanded_course is not None:
#                     if filtered_application is None:
#                         current_application = Application.objects.create(applicant_id=applicant.id,
#                                                                          demanded_course_id=course_id)
#                         current_application.save()
#                         complete_application_form = CompleteApplicationModelForm(request.POST, request.FILES, instance=current_application)
#                         if complete_application_form.is_valid():
#                             complete_application_form.save()
#                             return redirect('/application_list')
#                         context = {
#                             'demanded_course': demanded_course,
#                             'applicant': applicant,
#                             'current_application': current_application,
#                             'application_form': complete_application_form,
#                         }
#
#                     else:
#                         return JsonResponse({'status': 'Already Regisred'})
#                 else:
#                     return JsonResponse({'status': 'Not Found'})
#             else:
#                 return JsonResponse({'status': 'Not eligible User_type'})
#         else:
#             return JsonResponse({'status': 'Not Auth'})
#         return render(request, 'application/complete_application.html', context)


def add_course_to_application(request: HttpRequest):
    course_id = request.GET.get('course_id')
    applicant = User.objects.filter(id=request.user.id).first()
    if applicant.is_authenticated:
        if applicant.user_type_id == 3 or applicant.user_type_id == 4:
            demanded_course = Course.objects.filter(id=course_id).first()
            if demanded_course is not None:
                previous_application = Application.objects.filter(applicant_id=applicant.id, is_active=False).all()
                if previous_application is not None:
                    previous_application.delete()
                    application = Application.objects.create(applicant_id=applicant.id,
                                                                     demanded_course_id=demanded_course.id)

                    application.save()
                else:
                    application = Application.objects.create(applicant_id=applicant.id,
                                                             demanded_course_id=demanded_course.id)
                    application.save()
                return JsonResponse({'satatus' : 'sussesflly added'})

            else:
                return JsonResponse({'status': 'Not found'})
        else:
                return JsonResponse({'status': 'Not eligible'})
    else:
        return JsonResponse({'status': 'Not-Auth'})


class CompleteApplication(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        school = PublicPlace.objects.filter(applicant__user_id=request.user.id).first()
        current_application=Application.objects.filter(applicant=current_user, is_active=False).first()
        if current_application is not None:
            if school is not None:
                current_application.venue_id = school.id
                current_application.save()
        application_form = CompleteApplicationModelForm(instance=current_application)
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/complete_application.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        school = PublicPlace.objects.filter(applicant__user_id=request.user.id).first()
        current_application = Application.objects.filter(applicant=current_user, is_active=False).first()
        if current_application is not None:
            application_form = CompleteApplicationModelForm(request.POST, instance=current_application)
            if application_form.is_valid():
                current_application.is_active=True
                application_form.save()
                return redirect(reverse('application_list'))
        context = {
            'application': current_application,
            'application_form': application_form,
            'current_user': current_user
        }
        return render(request, 'application/complete_application.html', context)










