from django import forms
from .models import Persona, Actividad


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'actividades')

class ActividadForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=('nombre','descripcion','fecha','hora')

def __init__ (self, *args, **kwargs):

        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields["actividades"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actividades"].help_text = "Ingrese las actividades de la persona"
        self.fields["actividades"].queryset = Actividad.objects.all()
