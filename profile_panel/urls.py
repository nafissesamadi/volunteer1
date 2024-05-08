from django.urls import path

from profile_panel import views

urlpatterns=[
    path('',views.user_panel_page,name="user_panel_page"),
    path('profile', views.CompleteUserProfile.as_view(), name="user_profile_page"),
    path('school-profile', views.CompleteSchoolProfile.as_view(), name="school_profile_page"),
    path('institute-profile', views.CompleteInstituteProfile.as_view(), name="institute_profile_page"),
    path('student-profile', views.CompleteStudentProfile.as_view(), name="student_profile_page")
]