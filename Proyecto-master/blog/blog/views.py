from django.shortcuts import render

def Inicio(request):
    return render(request, 'index.html')

def Contacto(request):
    return render(request, 'contacto.html')

def Nosotros(request):
    return render(request, 'nosotros.html')


def Home(request):
	return render(request,'noticias/noticias.html')