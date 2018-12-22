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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from pgmanager.views import pgm_create_view, pgm_update_view,\
pgm_delete_view, pgmanagers_view, home_view, register_view,\
login_view,signout_view, pgmanagers_detailed_view
from django.views.generic import TemplateView, ListView, CreateView,\
UpdateView, DeleteView
from pgmanager.models import PG, Room
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^api/', include("api.urls")),
    url(r'^admin/', admin.site.urls),
    url(r'^pgmanager_create/', pgm_create_view),
    url(r'^pgmanager_update/([0-9]+)', pgm_update_view),
    url(r'^pgmanager_delete/([0-9]+)', pgm_delete_view),
    url(r'^pgmanagers/(?P<pk>[0-9]+)', pgmanagers_detailed_view),
    url(r'^pgmanagers/$', pgmanagers_view),
    url(r'^$',TemplateView.as_view(
        template_name="pgmanager/index.html")),
    url(r'^home/', home_view),
    url(r'^register/', register_view),
    url(r'^register/', register_view),
    url(r'^login/', login_view),
    url(r'^signout/', signout_view),
    url(r'^pgs/', ListView.as_view(
        model=PG,
        #template_name="pgmanager/",
        #queryset=PG.objects.all(),
        # fields=
        )),
    url(r'^pg_create/',CreateView.as_view(
        model=PG,
        fields="__all__",
        success_url='/pgs/'
        )),
    url(r'^pg_update/(?P<pk>[0-9]+)',UpdateView.as_view(
        model=PG,
        fields="__all__",
        success_url='/pgs/'
        )),
    url(r'^pg_delete/(?P<pk>[0-9]+)',DeleteView.as_view(
        model=PG,
        success_url='/pgs/'
        )),
    url(r'^room_create/',CreateView.as_view(
        model=Room,
        fields="__all__",
        success_url='/rooms/'
        )),
    url(r'^room_update/(?P<pk>[0-9]+)',UpdateView.as_view(
        model=Room,
        fields="__all__",
        success_url='/rooms/'
        )),
    url(r'^room_delete/(?P<pk>[0-9]+)',DeleteView.as_view(
        model=Room,
        success_url='/rooms/'
        )),
    url(r'^rooms/',ListView.as_view(
        model=Room
        )),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)