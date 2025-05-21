from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)# Nombre del curso
    description = models.TextField()# Descripción del curso
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)# Precio opcional
    duration = models.CharField(max_length=50, null=True, blank=True) # Duración del curso (ejemplo: "4 semanas")

    created_at = models.DateTimeField(auto_now_add=True) # Fecha de creación

    
    def __str__(self):
        return self.title# Mostrar el título en el panel de administración