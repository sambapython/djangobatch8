from django import forms
from pgmanager.models import PGManager, UserProfile
class PGManagerForm(forms.ModelForm):
	class Meta:
		model=PGManager
		fields=("name","gender","cell","email") #"__all__"

class PGManagerSeacrhForm(forms.Form):
	name = forms.CharField(max_length=60, required=False)
	gender = forms.ChoiceField(choices=PGManager.gender_choices,
	 required=False) 
	cell = forms.CharField(max_length=14, required=False)
	email = forms.EmailField(required=False)
	page = forms.IntegerField(required=False)
class UserPfrofileCreation(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields=("username","password","email","cell","role")


