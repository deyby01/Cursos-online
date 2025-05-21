from django.urls import path
from .views import dashboard, course_list

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', course_list, name='course_list')
]