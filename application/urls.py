from django.urls import path
from . import views

urlpatterns = [
    # path('',views.application_list, name='application_list'),
    path('',views.ApplicationListView.as_view(), name='application_list'),
    path('<int:pk>', views.ApplicationDetailView.as_view(), name='application_detail'),
    # path('<int:application_id>',views.application_detail, name='application_detail'),
    path('application-favorite',views.AddMyFavoriteApplication.as_view(), name='application_favorite'),
    path('courses',views.CoursesListView.as_view(), name='courses_list'),
    path('cat/<str:category>', views.CoursesListView.as_view(), name='courses_by_category_list'),
    path('cat/<str:category>/<str:major>', views.CoursesListView.as_view(), name='courses_by_category_major'),


]