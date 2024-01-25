from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index_page.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['data']= 'This is data in home page'
        context['message'] = 'This is a message in home page'
        return context


def header_partial(request):
    return render(request, 'shared/header_partial.html')


def footer_partial(request):
    return render(request, 'shared/footer_partial.html')


def canvas_partial(request):
    return render(request, 'shared/canvas_partial.html')
