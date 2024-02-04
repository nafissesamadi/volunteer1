from django.urls import path

from profile_panel import views

urlpatterns=[
    path('',views.CompleteUserProfile.as_view(),name="user_panel_page"),

]