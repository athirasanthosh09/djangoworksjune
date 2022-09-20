"""store URL Configuration

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
#from api.views import ProductsView,MorningView,EveningView,AddView,SubView
from api.views import CubeView,NumcheckView,FactView,WordcountView,\
    PrimeView,PallindromeView,ArmstronView,\
    ProductView,ProductDetailView,ReviewsView,ReviewDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cube",CubeView.as_view()),
    path("ncheck",NumcheckView.as_view()),
    path("factorial",FactView.as_view()),
    path("wordcount",WordcountView.as_view()),
    path("prime",PrimeView.as_view()),
    path("pallin",PallindromeView.as_view()),
    path("armstrong",ArmstronView.as_view()),
    path("product",ProductView.as_view()),
    path("product/<int:id>",ProductDetailView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailView.as_view()),
#     path("products",ProductsView.as_view()),
#     path("morning",MorningView.as_view()),
#     path("evening",EveningView.as_view()),
#     path("add",AddView.as_view()),

 ]
