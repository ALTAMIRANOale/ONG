from django.urls import path

from . import views

# LA URL EMPIEZA CON Noticias/ <este archivo>

app_name = 'noticias'

urlpatterns = [
    
    path('listar/', views.Listar, name = 'listar_noticias'),
    path('addnoticia/', views.AddNoticia.as_view(), name = 'addnoti'),

    # URL PARA VISTA BASADA EN FUNCION
    #path('detalle/<int:pk>', views.Detalle_Noticia_Funcion, name = 'detalle_noticias'),
    # URL PARA VISTA BASADA EN CLASE
    path('detalle/<int:pk>', views.Detalle_Noticia_Clase.as_view(), name = 'detalle_noticias'),
    path('comentar/', views.ComentarNoticia.as_view(), name='comentar'),
    path('add_comentario/<int:pk>', views.Agregar_Comentario, name="agregar_comentario"),

]

