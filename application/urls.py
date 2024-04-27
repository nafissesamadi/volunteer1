from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApplicationListView.as_view(), name='application_list'),
    path('<int:pk>', views.ApplicationDetailView.as_view(), name='application_detail'),
    # path('<int:application_id>',views.application_detail, name='application_detail'),
    path('user-application-list',views.UserApplicationListView.as_view(), name='user_application_list_page'),
    path('volunteer-class-list',views.VolunteerclassListView.as_view(), name='volunteer_class_list_page'),
    path('application-favorite',views.AddMyFavoriteApplication.as_view(), name='application_favorite'),
    path('courses',views.CoursesListView.as_view(), name='courses_list'),
    path('cat/<str:category>', views.CoursesListView.as_view(), name='courses_by_category_list'),
    path('cat/<str:category>/<str:major>', views.CoursesListView.as_view(), name='courses_by_category_major'),
    path('accept-application', views.accept_application, name='accept_application'),
    path('add-course-to-application', views.add_course_to_application, name='add_course_to_application'),
    # path('add-course-to-application', views.AddCourseToApplication.as_view(), name='complete_application_page'),
    path('complete-application', views.CompleteApplication.as_view(), name='complete_application_page'),
    path('complete-accepted-application', views.CompleteAcceptedApplication.as_view(), name='complete_accepted_application_page'),
    path('remove-course', views.remove_course, name='remove_course'),
    path('remove-venue', views.remove_venue, name='remove_venue'),
    path('remove-application', views.remove_active_application, name='remove_active_application_page'),
    path('remove-app-from-volunteer', views.remove_app_from_volunteer, name='remove_app_from_volunteer'),
    path('edit-active-application/<int:application_id>', views.EditActiveApplication.as_view(), name='edit_active_application'),

]