from django.shortcuts import render
from django.contrib import messages
from .forms import PersonaForm
from organizador.models import Persona, Actividad



def base(request):
    return render(request, 'organizador/base.html', {})

def base_persona(request):
    return render(request, 'organizador/base_persona.html', {})

def lista_persona(request):
    personas=Persona.objects.all()
    return render(request,'organizador/lista_persona.html',{'personas':personas})

def base_actividad(request):
    return render(request, 'organizador/base_actividad.html', {})

def lista_actividad(request):
    actividades=Actividad.objects.all()
    return render(request,'organizador/lista_actividad.html',{'actividades':actividades})
