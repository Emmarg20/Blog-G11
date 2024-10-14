from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib import messages
from django.urls import reverse

from .forms import RegistroForm
# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'
     




# class logoutusuario(LogoutView):
#     template_name = 'usuarios/logout.html'

#     def get_success_url(self):
#         messages.success(self.request,'logout exitoso')

#         return reverse('logout')
