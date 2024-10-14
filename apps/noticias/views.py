from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy

from .forms import NotiForm, CategForm

@login_required
def cargarnoticias(request):
	comtexto = { 'form': NotiForm}
	if request.method == 'POST':
			form = NotiForm(data=request.POST, files=request.FILES)
			if form.is_valid():
					form.save()
					return redirect('noticias:listar') #nombre app:nombre url
			else:
				form = NotiForm()
	return render(request, "noticias/cargarnoticias.html", comtexto)
    #posts = Post.objects.all() #lista todas las tareas juntas

 #@login_required #ok
def Listar_Noticias(request):
	 
	contexto = { 'form': NotiForm() }

	id_categoria = request.GET.get('id',None)

	if id_categoria:
		noti = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		noti = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS
		contexto['noticias'] = noti
		cat = Categoria.objects.all().order_by('nombre')
		contexto['categorias'] = cat

	return render(request, 'noticias/listar.html', contexto)



@login_required #ok
def eliminarnoticias(request, id): #ok
		Noti = get_object_or_404(Noticia, id=id) 
		if request.method == "POST":
			Noti.delete()
			return redirect("noticias:listar")
		return render(request, "noticias/eliminarnoticia.html", {'Noticia': Noticia})

@login_required #ok
def editar_noticia(request, pk):
    noti = get_object_or_404(Noticia, pk=pk)


    if request.method == 'POST':
        form = NotiForm(request.POST, request.FILES, instance=noti)
        if form.is_valid():
            form.save()
            return redirect('noticias:listar')  # Redirige a la vista de detalle
    else:
        form = NotiForm(instance=noti)

    return render(request, 'noticias/editarnoticia.html', {'form': form, 'noticia': noti})

#@login_required
def Detalle_Noticias(request, pk):
	contexto = {}
	noti = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO 
	contexto['noticia'] = noti

	c = Comentario.objects.filter(noticia = noti)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	comentar = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))
#	return redirect('noticias:detalle')


@login_required 
def eliminarmicomentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)

    if comentario.usuario == request.user:
        noticia_id = comentario.noticia.id
        comentario.delete()  # Elimina el comentario
        return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noticia_id}))  
    else:
        return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': comentario.noticia.id}))



#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''