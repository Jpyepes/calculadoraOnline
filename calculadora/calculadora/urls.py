"""calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from calculadora.views import index, sobreNosotros, pageBiseccion, pagePuntoFijo, pageNewton, pageReglaFalsa,pageMetodoSecante, pageGauss,settingsGauss, pageFactorizacionLU, pageSOR,  pageJacobiGauss, pageCDC, pageVandermonde, pageSpline, pageGraficas, pageLagrange, pageNewtonint,pageRaicesMultiples, pageBusquedasIncrementales
from calculadora.metodos import Biseccion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('sobreNosotros/', sobreNosotros, name="sobreNosotros"),
    path('pageBusquedasIncrementales/', pageBusquedasIncrementales, name = "pageBusquedasIncrementales"),
    path('pageBiseccion/', pageBiseccion, name="pageBiseccion"),
    path('pagePuntoFijo/', pagePuntoFijo, name="pagePuntoFijo"), 
    path('pageNewton/', pageNewton, name="pageNewton"),
    path('pageReglaFalsa/', pageReglaFalsa, name="pageReglaFalsa"),
    path('pageMetodoSecante/', pageMetodoSecante, name="pageMetodoSecante"),
    path('pageGauss/', pageGauss, name='pageGauss'),
    path('settingsGauss/', settingsGauss, name='settingsGauss'),
    path('pageFactorizacionLU/', pageFactorizacionLU, name='pageFactorizacionLU'),
    path('pageSOR/', pageSOR, name="pageSOR"),
    path('pageJacobiGauss/', pageJacobiGauss, name="pageJacobiGauss"),
    path('pageCDC/', pageCDC, name="pageCDC"),
    path('pageVandermonde/', pageVandermonde, name="pageVandermonde"),
    path('pageSpline/', pageSpline, name="pageSpline"),
    path('pageGraficas/', pageGraficas, name="pageGraficas"),
    path('pageLagrange/', pageLagrange, name="pageLagrange"),
    path('pageNewtonint/', pageNewtonint, name="pageNewtonint"),
    path('pageRaicesMultiples/', pageRaicesMultiples, name="pageRaicesMultiples"),
]
