# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from pgmanager.models import PGManager
from rest_framework.response import Response
from rest_framework import status

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
		return Response("PGManager created successfully",
			status=status.HTTP_201_CREATED)
	def put(self, format=None,pk=None):
		pgm_inst = PGManager.objects.get(id=pk)
		req_data = self.request.data 
		if "name" in req_data:
			pgm_inst.name = req_data["name"]
		if "gender" in req_data:
			pgm_inst.gender = req_data["gender"]
		if "email" in req_data:
			pgm_inst.email = req_data["email"]
		if "cell" in req_data:
			pgm_inst.cell = req_data["cell"]
		try:
			pgm_inst.save()
		except Exception as err:
			return Response("Issiue: %s"%err.message,
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response("Record updated successfully")

	def delete(self, format=None, pk=None):
		pgm_inst = PGManager.objects.filter(id=pk)
		if pgm_inst:
			pgm_inst=pgm_inst[0]
			pgm_inst.delete()
			return Response("Record deleted successfully")
		else:
			return Response("No record found",
				status=status.HTTP_404_NOT_FOUND)
