from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApplicationListView.as_view(), name='application_list'),
    path('ongoing-application',views.OngoingApplicationListView.as_view(), name='ongoing_application_list'),
    path('<int:pk>', views.ApplicationDetailView.as_view(), name='application_detail'),
    # path('<int:application_id>',views.application_detail, name='application_detail'),
    path('user-application-list',views.UserApplicationListView.as_view(), name='user_application_list_page'),
    path('volunteer-class-list',views.VolunteerclassListView.as_view(), name='volunteer_class_list_page'),
    path('application-favorite',views.AddMyFavoriteApplication.as_view(), name='application_favorite'),
    path('courses',views.CoursesListView.as_view(), name='courses_list'),
    path('cat/<str:category>', views.CoursesListView.as_view(), name='courses_by_category_list'),
    path('cat/<str:category>/<str:major>', views.CoursesListView.as_view(), name='courses_by_category_major'),
    path('venues/app/<int:app>',views.PublicPlaceListView.as_view(), name='publicplaces_list'),
    path('venues',views.PublicPlaceListView.as_view(), name='publicplace_list'),
    # path('venues/<int:pk>', views.PublicPlaceDetailView.as_view(), name='publicplace_detail'),
    path('venues/app/<int:app>/<int:pk>', views.PublicPlaceDetailView.as_view(), name='publicplace_detail_with_app'),
    path('venuetype/<str:venuetype>', views.PublicPlaceListView.as_view(), name='venues_by_type'),
    path('accept-application', views.accept_application, name='accept_application'),
    path('add-course-to-application', views.add_course_to_application, name='add_course_to_application'),
    path('add-venue', views.add_venue_to_application, name='add_venue_to_application'),
    path('complete-application', views.CompleteApplication.as_view(), name='complete_application_page'),
    path('complete-accepted-application', views.CompleteAcceptedApplication.as_view(), name='complete_accepted_application_page'),
    path('remove-course', views.remove_course, name='remove_course'),
    path('remove-venue', views.remove_venue, name='remove_venue'),
    path('remove-application', views.remove_active_application, name='remove_active_application_page'),
    path('remove-inactive-application', views.remove_inactive_application, name='remove_inactive_application_page'),
    path('remove-app-from-volunteer-list', views.remove_app_from_volunteer, name='remove_app_from_volunteer'),
    path('remove-venue-of-application', views.remove_venue_in_edit_mode, name='remove_venue_in_edit_mode'),
    path('remove-accepted-application', views.remove_accepted_application_by_volunteer, name='remove_accepted_application'),
    path('edit-active-application/<int:application_id>', views.EditActiveApplication.as_view(), name='edit_active_application'),

]