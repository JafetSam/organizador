from django import forms
from .models import Persona, Actividad


class PersonaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'actividades')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


def __init__ (self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["actividades"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["actividades"].help_text = "Ingrese las actividades de la persona"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["actividades"].queryset = Actividad.objects.all()
