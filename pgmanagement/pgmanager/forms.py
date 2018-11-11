from django import forms
from pgmanager.models import PGManager
class PGManagerForm(forms.ModelForm):
	class Meta:
		model=PGManager
		fields=("name","gender","cell","email") #"__all__"

