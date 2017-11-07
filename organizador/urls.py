from django.conf.urls import url
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.base),
    url(r'^base_persona/$', views.base_persona, name='base_persona'),
    url(r'^lista_persona/$', views.lista_persona, name='lista_persona'),
    url(r'^base_actividad/$', views.base_actividad, name='base_actividad'),
    url(r'^lista_actividad/$', views.lista_actividad, name='lista_actividad'),
    url(r'^nueva_persona/$', views.nueva_persona, name='nueva_persona'),
    url(r'^nueva_actividad/$', views.nueva_actividad, name='nueva_actividad'),
    url(r'^editar_persona/(?P<pk>[0-9]+)/$', views.editar_persona, name='editar_persona'),
    url(r'^editar_actividad/(?P<pk>[0-9]+)/$', views.editar_actividad, name='editar_actividad'),
    url(r'^eliminar_persona/(?P<pk>[0-9]+)/$', views.eliminar_persona, name='eliminar_persona'),
    url(r'^eliminar_actividad/(?P<pk>[0-9]+)/$', views.eliminar_actividad, name='eliminar_actividad'),
    ]
