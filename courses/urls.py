from django.urls import path
from .views import dashboard, course_list, enroll_course, enrolled_courses

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', course_list, name='course_list'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('my-courses/', enrolled_courses, name='enrolled_courses'),
]