from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(), name='home_page'),
    # path('site-header',views.header_partial, name='header_partial'),

]