from django.forms import ModelForm
from .models import Personal_info

class Personal_infoForm(ModelForm):
	class Meta:
		model= Personal_info
		fields= '__all__'