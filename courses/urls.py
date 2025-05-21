from django.urls import path
from .views import dashboard, course_list, enroll_course

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', course_list, name='course_list'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
]