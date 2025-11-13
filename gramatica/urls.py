from django.urls import path
from . import views

app_name = 'gramatica'  # Namespace

urlpatterns = [
    path('', views.lista_regras, name='lista_regras'),

    path('analisar/', views.analisador_view, name='analisador'),
]