from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)# Nombre del curso
    description = models.TextField()# Descripción del curso
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)# Precio opcional
    duration = models.CharField(max_length=50, null=True, blank=True) # Duración del curso (ejemplo: "4 semanas")

    created_at = models.DateTimeField(auto_now_add=True) # Fecha de creación

    
    def __str__(self):
        return self.title# Mostrar el título en el panel de administración
    

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario inscrito
    course = models.ForeignKey('Course', on_delete=models.CASCADE)  # Curso al que se inscribe
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Fecha de inscripción

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
