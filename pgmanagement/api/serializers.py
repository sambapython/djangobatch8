from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
from pgmanager.models import PGManager
class PGManagerSerializer(ModelSerializer):
	class Meta:
		model=PGManager
		fields=["name","cell","gender"]  #"__all__"
class PGManagerCreateSerializer(ModelSerializer):
	class Meta:
		model=PGManager
		fields="__all__"
	def validate_name(self, value):
		print "validation called@@@@@@@@@@@@"
		return value
	def validate_gender(self, value):
		if value not in ["F","M"]:
			raise Exception("expectiogn M or F. giving %s"%value)
		return value
	def validate_cell(self, value):
		if len(value)!=10:
			raise ValidationError("Expeting 10 digits.")
		return value
	def validate_email(self, value):
		if "@" not in value:
			raise Exception("not a valid email")
		return value
# class PGManagerUpdateSerializer(serializers.Serializer):
# 	name=serializers.SlugField(max_length=60, required=False)
# 	gender=serializers.ChoiceField(PGManager.gender_choices,required=False)
# 	cell=serializers.CharField(max_length=10,required=False)
# 	email = serializers.EmailField(required=False)
	
# 	def validate_cell(self, value):
# 		if len(value)!=10:
# 			raise ValidationError("Expeting 10 digits.")
# 		return value
class PGManagerUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=PGManager
		fields=("name","cell","email","gender")
		extra_kwargs={"cell":{"required":False},
						"name":{"required":False},
						"email":{"required":False},
						"gender":{"required":False}}

	def validate_cell(self, value):
		if len(value)!=10:
			raise ValidationError("Expeting 10 digits.")
		return value



