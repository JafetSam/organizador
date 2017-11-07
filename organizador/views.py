from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import PersonaForm,ActividadForm
from organizador.models import Persona, Actividad,TareasPersona
from django.contrib.auth.decorators import login_required

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


@login_required
def nueva_persona(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():

            persona = Persona.objects.create(nombre=formulario.cleaned_data['nombre'], apellido= formulario.cleaned_data['apellido'])

            for actividad_id in request.POST.getlist('actividades'):

                t =TareasPersona(actividad_id=actividad_id, persona_id = persona.id)
                t.save()

            return redirect('lista_persona')
    else:
        formulario = PersonaForm()
    return render(request, 'organizador/nueva_persona.html', {'formulario': formulario})

@login_required
def nueva_actividad(request):
    if request.method == "POST":
        formulario = ActividadForm(request.POST)
        if formulario.is_valid():

            acitividad = Actividad.objects.create(
            nombre=formulario.cleaned_data['nombre'],
            descripcion= formulario.cleaned_data['descripcion'],
            fecha=formulario.cleaned_data['fecha'],
            hora=formulario.cleaned_data['hora'],
            )


            return redirect('lista_actividad')
    else:
        formulario = ActividadForm()
    return render(request, 'organizador/nueva_actividad.html', {'formulario': formulario})





@login_required
def editar_persona(request,pk):
    persona=get_object_or_404(Persona,pk=pk)
    if request.method =="POST":
        form=PersonaForm(request.POST,instance=persona)

        if form.is_valid():
            persona=form.save(commit=False)
            persona.save()
            return redirect('lista_persona')
    else:
        form=PersonaForm(instance=persona)
    return render(request,'organizador/editar_persona.html',{'form':form})



@login_required
def editar_actividad(request,pk):
    actividad=get_object_or_404(Actividad,pk=pk)
    if request.method =="POST":
        form=ActividadForm(request.POST,instance=actividad)

        if form.is_valid():
            actividad=form.save(commit=False)
            actividad.save()
            return redirect('lista_actividad')
    else:
        form=ActividadForm(instance=actividad)
    return render(request,'organizador/editar_actividad.html',{'form':form})




@login_required
def eliminar_persona(request,pk):
    persona=get_object_or_404(Persona,pk=pk)
    persona.delete()
    return redirect('lista_persona')

@login_required
def eliminar_actividad(request,pk):
    actividad=get_object_or_404(Actividad,pk=pk)
    actividad.delete()
    return redirect('lista_actividad')
