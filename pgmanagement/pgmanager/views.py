# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from pgmanager.models import PGManager

# Create your views here.
def pgm_create_view(request):
	# read templates/pgm_create.html
	#return HttpResponse(resp)
	message=""
	if request.method=="POST":
		data = request.POST
		try:
			pgm = PGManager(name=data["name"],
				gender=data["gender"],
				email=data["email"],
				cell=data["cell"])
			pgm.save()
			message="pgmanager created successfully"
		except Exception as err:
			print "ERROR:",err
			message="creation failed: %s"%err

	return render(request,"pgmanager/pgm_create.html",
		{"message":message})
