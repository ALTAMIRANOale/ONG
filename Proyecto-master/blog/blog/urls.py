
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

#URL LOGIN
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name = 'inicio'),
    path('Acercade/contacto', views.Contacto, name='contacto'),
    path('Acercade/nosotros', views.Nosotros, name= 'nosotros'),
    path('noticia/', views.Home, name = 'home'),
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

    #URL DE APLICACIONES
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuario/',include('apps.usuarios.urls'))

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
