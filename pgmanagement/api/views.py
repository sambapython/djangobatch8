# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from pgmanager.models import PGManager
from rest_framework.response import Response

# Create your views here.
class PGManagerAPIView(APIView):
	def get(self, format=None):
		data = PGManager.objects.all()
		data_resp = [{"name":obj.name,"cell":obj.cell} for obj in data]
		return Response(data_resp)

	def post(self, format=None):
		req_data = self.request.data
		#pgm = PGManager(name=data["name"],cell=data["cell"],
		# gender=data["gender"],email=data["email"])
		pgm = PGManager(**req_data)
		pgm.save()
		return Response("PGManager created successfully")
	def put(self, format=None,pk=None):
		pass
	def delete(self, format=None, pk=None):
		pass
