# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
# Create your models here.

def namevalidation(value):
	if not value.isalnum():
		raise ValidationError("not a valid name")
# def cellvalidation(value):
# 	if not value.isdigit():
# 		raise ValidationError("Expecting only 10 digit number")
# 	elif len(value)!=10:
# 		raise ValidationError("Expecting only 10 digit number")

class UserProfile(AbstractUser):
	roles=[('s',"Student"),("p","PGManager")]
	cell = models.CharField(max_length=10)
	role=models.CharField(choices=roles,default="s", max_length=1)


class AbstractPGManager(models.Model):
	name=models.CharField(max_length=60, 
		validators=[namevalidation])
	status = models.BooleanField(default=True)
	class Meta:
		abstract=True

class PGManager(AbstractPGManager):
	# pg_id = models.IntegerField(primary_key=True)
	gender_choices = [('M',"Male"),
						("F","Female")]
	gender=models.CharField(choices=gender_choices,
		max_length=2)
	cell = models.CharField(max_length=14,unique=True)
	email = models.EmailField(unique=True)

	def __str__(self):
		return "%s, %s"%(self.name,self.cell)
	


class PG(AbstractPGManager):
	address=models.TextField(max_length=250)
	pgmanager=models.ForeignKey(PGManager, 
		on_delete=models.PROTECT)
	class Meta:
		db_table="pg"
		
class Room(AbstractPGManager):
	type_choices=[("AC","AC ROOM"),
				  ("NAC","Non AC ROOM")]
	pic = models.ImageField(blank=True)
	type=models.CharField(choices=type_choices, max_length=3)
	cost=models.IntegerField()
	strength=models.IntegerField(blank=True, default=1)
	pg = models.ForeignKey(PG, on_delete=models.PROTECT)

class Parent(models.Model):
	name=models.CharField(max_length=60)

class child1(Parent):
	status=models.BooleanField(default=True)
class child2(models.Model):
	parent=models.OneToOneField(Parent)
	status=models.BooleanField(default=True)

class Track(models.Model):
	url=models.CharField(max_length=250, blank=True)
	status_cod=models.IntegerField(blank=True)

