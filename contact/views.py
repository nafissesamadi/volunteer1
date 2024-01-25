from django.shortcuts import render
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfile
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView


# Create your views here.


# def contact_us_page(request):
#     if request.method == 'POST':
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('application_list')
#
#     else:
#         contact_form = ContactUsModelForm()
#     return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})

# class ContactUsView(View):
#     def get(self,request):
#         contact_form=ContactUsModelForm()
#         return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})
#     def post(self,request):
#         contact_form=ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('application_list')
#         return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})


# class ContactUsView(FormView):
#     template_name = 'contact/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact/contact_us_page.html'
    success_url = '/contact-us/'


# def store_file(file):
#     with open('temp/image.jpg', "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'contact/create_profile_page.html', {'form': form})
#
#     def post(self, request):
#         submitted_form=ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return redirect('/contact-us/create-profile')
#         return render(request, 'contact/create_profile_page.html', {'form': submitted_form})

class CreateProfileView(CreateView):
    template_name='contact/create_profile_page.html'
    model=UserProfile
    fields='__all__'
    success_url = '/contact-us/create-profile'


class ProfilesView(ListView):
    model=UserProfile
    template_name = 'contact/profiles_list_page.html'
    context_object_name = 'profiles'
