# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from pgmanager.models import PGManager
from pgmanager.forms import PGManagerForm

# Create your views here.
def pgm_delete_view(request, pk):
	message=""
	pgm_instance = PGManager.objects.get(id=pk)
	form = PGManagerForm(instance=pgm_instance)
	if request.method=="POST":
		pgm_instance.delete()
		message="record deleted successfully!!"
		form = PGManagerForm()
	return render(request,"pgmanager/pgm_delete_form.html",
		{"message":message,"form":form})

def pgm_update_view(request, pk):
	message=""
	pgm_instance=PGManager.objects.get(id=pk)
	if request.method=="POST":
		form=PGManagerForm(data=request.POST,
			instance=pgm_instance)
		if form.is_valid():
			form.save()
			message="PGMANAGER updated successfully"
		else:
			message=form._errors
	pgm_instance=PGManager.objects.get(id=pk)
	form = PGManagerForm(instance=pgm_instance)
	return render(request, "pgmanager/pgm_update_form.html",
		{"message":message, "form":form})


def pgm_create_view(request):
	# read templates/pgm_create.html
	#return HttpResponse(resp)
	message=""
	form = PGManagerForm()
	if request.method=="POST":
		#data = request.POST
		try:
			'''
			pgm = PGManager(name=data["name"],
				gender=data["gender"],
				email=data["email"],
				cell=data["cell"])
			pgm.save()
			'''
			form=PGManagerForm(data=request.POST)
			if form.is_valid():
				form.save()
				message="pgmanager created successfully"
			else:
				message=form._errors
		except Exception as err:
			print "ERROR:",err
			message="creation failed: %s"%err

	return render(request,"pgmanager/pgm_create_form.html",
		{"message":message,"form":form})
