
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'noticias'

urlpatterns = [
	
	

	path('', views.Listar_Noticias, name = 'listar'),
    
	#path('', views.misrecientes, name='misrecientes'),
    
	path('cargarnoticia/', views.cargarnoticias, name='cargar_noticia'),

	path('Eliminarnoticia/<int:id>/', views.eliminarnoticias, name = 'eliminar_noticia'),
    
	path('noticia/editar/<int:pk>/', views.editar_noticia, name='editar_noticia'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    
	path('comentarios/eliminar/<int:comentario_id>/', views.eliminarmicomentario, name='eliminarmicomentario'),
	
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)