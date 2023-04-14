from django.urls import path
from candidato.views import *

app_name = 'candidato'

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path(r'apresenta/', ApresentaTins.as_view(), name='apresenta'),
    path(r'fit_parte01/<str:email>', NovoFitCult01.as_view(), name='criarfit01'),
    path(r'fit_parte01altera/<str:cpf>', NovoFitCult01Edita.as_view(), name='criarfit01edita'),
    path(r'fit_parte02/<str:cpf>', NovoFitCult02.as_view(), name='criarfit02'),
    path(r'fit_parte02altera/<str:cpf>', NovoFitCult02Edita.as_view(), name='criarfit02edita'),
    path(r'fit_parte03/<str:cpf>', NovoFitCult03.as_view(), name='criarfit03'),
    path (r'fit_parte03altera/<str:cpf>', NovoFitCult03Edita.as_view (), name='criarfit03edita'),
    path(r'fit_parte04/<str:cpf>', ContFitCult01.as_view(), name='contpt01'),
    path(r'fit_parte05/<str:cpf>', ContFitCult02.as_view(), name='contpt02'),
    path(r'fit_parte06/<str:cpf>', ContFitCult03.as_view(), name='contpt03'),
    path(r'fit_parte07/<str:cpf>', ContFitCult04.as_view(), name='contpt04'),
    path(r'fit_parte08/<str:cpf>', ContFitCult05.as_view(), name='contpt05'),
    path(r'fit_parte09/<str:cpf>', ContFitCult06.as_view(), name='contpt06'),
    path(r'fit_parte10/<str:cpf>', ContFitCult07.as_view(), name='contpt07'),
    path(r'fit_parte11/<str:cpf>', ContFitCult08.as_view(), name='contpt08'),
    path(r'fit_parte12/<str:cpf>', ContFitCult09.as_view(), name='contpt09'),
    path(r'fit_parte13/<str:cpf>', ContFitCult10.as_view(), name='contpt10'),
    path(r'finaliza/', FinalizaFit.as_view(), name='finaliza'),
]
