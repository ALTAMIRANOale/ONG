from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Noticia,Comentario

def Listar(request):
	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Noticia.objects.all()
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'noticias/noticia2.html',ctx)


class AddNoticia(CreateView):
	model = Noticia
	fields = ['autor', 'titulo', 'cuerpo', 'imagen', 'categoria']
	template_name = 'noticias/addNoticia.html'
	success_url = reverse_lazy('noticias:listar_noticias')

# EJEMPLO DE COMO DESARMA EL CTX EL TEMPLATE.
# ctx['wilson'] = 'wilson'
# ctx['notas'] = [5,6,9]
# EL TEMPLATE ya separa el diccionario
# nombre = 'wilson'
# notas = [5,6,9]


#VISTA BASADA EN FUNCIONES
@login_required
def Detalle_Noticia_Funcion(request, pk):
	ctx = {}
	noticia = Noticia.objects.get(pk = pk)
	ctx['resultado'] = noticia
	return render(request,'noticias/detallenoticia.html',ctx)

#VISTA BASADA EN CLASES
class Detalle_Noticia_Clase(LoginRequiredMixin, DetailView):
	model = Noticia
	template_name = 'noticias/detalle2.html'

class ComentarNoticia(ListView):
    model=Noticia
    template_name = 'noticias/agregarnoticia.html'

#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LLAMA:
# SI ES UNO SOLO object
# SI SON MUCHOS SE LLAMA obect_list


def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('coment')
	
	#Forma 1 (es la mejor para este caso)
	noti = Noticia.objects.get(pk = pk)

	c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticias' , kwargs={'pk':pk}))
