from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]