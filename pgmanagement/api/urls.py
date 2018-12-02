from django.conf.urls import url, include
from api.views import PGManagerAPIView
urlpatterns = [
	url(r'^pgmanagers/(?P<pk>[0-9]+)', PGManagerAPIView.as_view()),
    url(r'^pgmanagers/$', PGManagerAPIView.as_view()),
    ]