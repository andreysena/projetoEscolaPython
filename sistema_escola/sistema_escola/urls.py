"""sistema_escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from escola.views import mostrarindex, cadprof, listaprof, altprof, delprof,\
                                       cadfunc, listafunc, altfunc, delfunc,\
                                       cadmat, listamat, altmat, delmat,\
                                       cadcoord, listacoord, altcoord, delcoord,\
                                       cadturma, listaturma, altturma, delturma,\
                                       cadaluno, listaaluno, altaluno, delaluno


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', mostrarindex, name="url_index"),

    path("listaFuncionario/", listafunc, name="url_listagemFunc"),
    path("cadFuncionario/", cadfunc, name="url_cadastroFunc"),
    path('altFuncionario/<int:pk>', altfunc, name="url_atualizarFunc"),
    path('delFuncionario/<int:pk>', delfunc, name="url_deletaFunc"),

    path("listaMateria/", listamat, name="url_listagemMat"),
    path("cadMateria/", cadmat, name="url_cadastroMat"),
    path('altMateria/<int:pk>', altmat, name="url_atualizarMat"),
    path('delMateria/<int:pk>', delmat, name="url_deletaMat"),

    path('listaProfessor/', listaprof, name="url_listagemProf"),
    path('cadProfessor/', cadprof, name="url_cadastroProf"),
    path('altProfessor/<int:pk>', altprof, name="url_atualizarProf"),
    path('delProfessor/<int:pk>', delprof, name="url_deletaProf"),

    path('listaCoordenador/', listacoord, name="url_listagemCoord"),
    path('cadCoordenador/', cadcoord, name="url_cadastroCoord"),
    path('altCoordenador/<int:pk>', altcoord, name="url_atualizarCoord"),
    path('delCoordenador/<int:pk>', delcoord, name="url_deletaCoord"),

    path('listaTurma/', listaturma, name="url_listagemTurma"),
    path('cadTurma/', cadturma, name="url_cadastroTurma"),
    path('altTurma/<int:pk>', altturma, name="url_atualizarTurma"),
    path('delTurma/<int:pk>', delturma, name="url_deletaTurma"),

    path('listaAluno/', listaaluno, name="url_listagemAluno"),
    path('cadAluno/', cadaluno, name="url_cadastroAluno"),
    path('altAluno/<int:pk>', altaluno, name="url_atualizarAluno"),
    path('delAluno/<int:pk>', delaluno, name="url_deletaAluno"),

]
