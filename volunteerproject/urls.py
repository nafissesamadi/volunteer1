"""
URL configuration for volunteerproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from setuptools.config._validate_pyproject.formats import url

urlpatterns = [
    path('register/', include('account.urls')),
    path('application/', include('application.urls')),
    path('', include('home.urls')),
    path('contact-us/', include('contact.urls')),
    path('profile/', include('profile_panel.urls')),
    path('admin/', admin.site.urls),
    path('chaining/', include("smart_selects.urls")),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



