"""simplemoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from simplemoc.core.views import home, home2, home3, home4

urlpatterns = {
    path('pessoas', home, name='pessoas'),
    path('custos', home2, name='custos'),
    path('pedidos/<int:id>/', home3, name='pedidos'),
    path('por_dia/<slug:data>/', home4, name='por_dia'),
    path('admin/', admin.site.urls),
}
