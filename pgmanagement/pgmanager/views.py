# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from pgmanager.models import PGManager
from pgmanager.forms import PGManagerForm, PGManagerSeacrhForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.
def login_view(request):
	form = AuthenticationForm()
	msg=""
	if request.method=="POST":
		data = request.POST
		username=data["username"]
		password=data["password"]
		user=authenticate(username=username, password=password)
		if user:
				msg="LOGIN SUCCESS"
		else:
				msg= "Invalid creadentials"
	return render(request,"pgmanager/login.html",
		{"form":form,"messages":msg})

def register_view(request):
	form = UserCreationForm()
	msg=""
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			msg="User created successfully"
		else:
			msg= form._errors
	return render(request,"pgmanager/reg.html",
		{"form":form,"messages":msg})
def home_view(request):
	return render(request,"pgmanager/home.html")
def index_view(request):
	return render(request,"pgmanager/index.html")

def pgmanagers_view(request):
	
	form = PGManagerSeacrhForm(request.POST)
	search_dict = {"status": True}
	if request.method=="POST":
		search_form=request.POST
		
		name=search_form["name"]
		gender = search_form["gender"]
		email = search_form["email"]
		if name:
			search_dict["name"]=name
		if gender:
			search_dict["gender"] =gender
		if email:
			search_dict["email"]=email

	objects=PGManager.objects.filter(**search_dict)
	#page_num = request.POST["page"]
	if "page" in request.POST:
		page_num = request.POST["page"]
		page_num = page_num if page_num else 1
	else:
		page_num=1
	records_per_page=10
	paginator = Paginator(objects,records_per_page)
	page_details = paginator.page(page_num)
	pagination_details = {"records":paginator.count,
	"currentpage":page_num,"recordsperpage":records_per_page,
	"num_page":paginator.num_pages}
	return render(request, "pgmanager/pgmanagers.html",
		{"data":page_details,
		"form":form,
		"page_details":pagination_details})

def pgm_delete_view(request, pk):
	message=""
	pgm_instance = PGManager.objects.get(id=pk)
	form = PGManagerForm(instance=pgm_instance)
	if request.method=="POST":
		pgm_instance.status=False
		pgm_instance.save()
		message="record deleted successfully!!"
		return redirect("/pgmanagers/")
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
			return redirect("/pgmanagers/")
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
		try:
			form=PGManagerForm(data=request.POST)
			if form.is_valid():
				form.save()
				return redirect("/pgmanagers/")
			else:
				message=form._errors
		except Exception as err:
			print ("ERROR:%s"%err)
			message="creation failed: %s"%err

	return render(request,"pgmanager/pgm_create_form.html",
		{"message":message,"form":form})
