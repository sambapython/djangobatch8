# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def namevalidation(value):
	if not value.isalnum():
		raise ValidationError("not a valid name")
def cellvalidation(value):
	if not value.isdigit():
		raise ValidationError("Expecting only 10 digit number")
	elif len(value)!=10:
		raise ValidationError("Expecting only 10 digit number")

class PGManager(models.Model):
	# pg_id = models.IntegerField(primary_key=True)
	gender_choices = [('M',"Male"),
						("F","Female")]
	name=models.CharField(max_length=60, 
		validators=[namevalidation])
	gender=models.CharField(choices=gender_choices,
		max_length=2)
	cell = models.CharField(max_length=14,
		validators=[cellvalidation], unique=True)
	email = models.EmailField(unique=True)
	status = models.BooleanField(default=True)


class PG(models.Model):
	name = models.CharField(max_length=60)
	address=models.TextField(max_length=250)
	pgmanager=models.ForeignKey(PGManager)
	status = models.BooleanField(default=True)
	class Meta:
		db_table="pg"
		
class Room(models.Model):
	type_choices=[("AC","AC ROOM"),
				  ("NAC","Non AC ROOM")]
	name=models.CharField(max_length=60)
	type=models.CharField(choices=type_choices, max_length=3)
	cost=models.IntegerField()
	strength=models.IntegerField(blank=True, default=1)
	status=models.BooleanField(default=True)
	pg = models.ForeignKey(PG)






