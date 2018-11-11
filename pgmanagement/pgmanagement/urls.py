"""pgmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from pgmanager.views import pgm_create_view, pgm_update_view,\
pgm_delete_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pgmanager_create/', pgm_create_view),
    url(r'^pgmanager_update/([0-9]+)', pgm_update_view),
    url(r'^pgmanager_delete/([0-9]+)', pgm_delete_view),

]
