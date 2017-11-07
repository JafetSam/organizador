from django.contrib import admin
from organizador.models import Persona, PersonaAdmin, Actividad, ActividadAdmin

#Registramos nuestras clases principales.
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Actividad, ActividadAdmin)
