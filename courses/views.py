from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'courses/dashboard.html')

def course_list(request):
    courses = Course.objects.all() #Obtener todos los cursos
    
    return render(request, 'courses/course_list.html', {'courses': courses}) #Pasar los cursos a la plantilla