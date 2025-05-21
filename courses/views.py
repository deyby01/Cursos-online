from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'courses/dashboard.html')

def course_list(request):
    courses = Course.objects.all() #Obtener todos los cursos
    
    return render(request, 'courses/course_list.html', {'courses': courses}) #Pasar los cursos a la plantilla

@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('course_list')  # Redirige de nuevo a la lista de cursos

@login_required
def enrolled_courses(request):
    courses = Enrollment.objects.filter(user=request.user).select_related('course')
    return render(request, 'courses/enrolled_courses.html', {'courses': courses})
