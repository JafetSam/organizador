from django.db import models
from django.contrib import admin


class Actividad(models.Model):
    nombre    = models.CharField(max_length=30)
    descripcion=models.CharField(max_length=80)
    fecha=models.DateField(max_length=10)
    hora=models.TimeField(default=0)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre  =   models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    actividades = models.ManyToManyField(Actividad, through='TareasPersona')

    def __str__(self):
        return self.nombre


class TareasPersona (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)


class TareasPersonaInLine(admin.TabularInline):
    model = TareasPersona
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1



class PersonaAdmin(admin.ModelAdmin):
    inlines = (TareasPersonaInLine,)


class ActividadAdmin (admin.ModelAdmin):
    inlines = (TareasPersonaInLine,)
