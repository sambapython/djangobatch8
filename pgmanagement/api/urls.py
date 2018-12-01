from django.conf.urls import url, include
from api.views import PGManagerAPIView
urlpatterns = [
    url(r'^pgmanagers/', PGManagerAPIView.as_view()),
    ]