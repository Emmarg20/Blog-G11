from django.db import models
from apps.usuarios.models import Usuario

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	titulo = models.CharField(max_length = 150,verbose_name= "Título", null=False)
	bajada = models.TextField(verbose_name= "Bajada")
	cuerpo = models.TextField(verbose_name= "Cuerpo")
	imagen = models.ImageField(upload_to = 'noticias/')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Campo nuevo

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.noticia}->{self.texto}"
	
	#eliminar la imagen al eliminar el post
	#def delete(self, using =None, keep_parents = False):
		#self.imagen.delete(self.imagen.name)
		#super().delete()
	
