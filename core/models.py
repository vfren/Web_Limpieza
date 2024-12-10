from django.db import models
from django.contrib import admin


# Create your models here. haré estas tablas para iniciar

# Tabla para usuarios (clientes)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Tabla para profesionales de limpieza
class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)  # API Google Maps

    def __str__(self):
        return self.nombre

# Tabla para las tareas o servicios ofrecidos
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Tabla para las citas entre usuarios y profesionales
class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tareas = models.ManyToManyField(Tarea)  # Relación muchos a muchos
    estado = models.CharField(
        max_length=20,
        choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')],
    )

    def __str__(self):
        return f"{self.usuario} - {self.profesional} ({self.fecha})"

# Tabla para calificaciones
class Calificacion(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()  # Por ejemplo, de 1 a 5
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cita} - {self.puntuacion}"
