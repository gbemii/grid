from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from adminstrator.models import *
from .forms import Personal_infoForm
# Create your views here.


def index_view(request, pk, *args, **kwargs):
	person= Personal_info.objects.get(id=pk)
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.get(id=pk)
	context= {'person': person, 'scheme': scheme, 'statement': statement
	}
	return render(request, "user/index.html", context)






	

def profile_view(request, pk, *args, **kwargs):
	person= Personal_info.objects.get(id=pk)
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.all()
	context= {'person': person, 'scheme': scheme, 'statement': statement
	}
	return render(request, "user/profile.html", context)


def setting_view(request, pk, *args, **kwargs):
	
	person= Personal_info.objects.get(id=pk)
	context={'person': person, 'first': 'joe'
	}
	return render(request, "user/profile-setting.html", context)


def login_activity_view(request, pk, *args, **kwargs):
	print(args, kwargs)
	person= Personal_info.objects.get(id=pk)
	context={'person': person, 'first': 'joe'
	}
	return render(request, "user/profile-activity.html", context)


def investment_view(request, pk, *args, **kwargs):
	
	person= Personal_info.objects.get(id=pk)
	statement= Account.objects.all()
	scheme= Investment_scheme.objects.all()
	context={'person': person, 'scheme': scheme, 'statement': statement 
	}
	return render(request, "user/schemes.html", context)

def investment_detail_view(request, pk, *args, **kwargs):
	
	person= Personal_info.objects.get(id=pk)
	statement= Account.objects.get(id=1)
	scheme= Investment_scheme.objects.get( id=pk )
	context={'person': person, 'scheme': scheme, 'statement': statement 
	}
	return render(request, "user/scheme-details.html", context)

def account_view(request, *args, **kwargs):
	statement= Account.objects.all()
	context= {'statement': statement
	}
	return render(request, "index.html", context)



def Update_profile(request, pk):
	project= Personal_info.objects.get(id=pk)

	form= Personal_infoForm(instance=project)
	context= { 'form':form }
	return render(request,'user/profile.html', context )


def farm_view(request, *args, **kwargs):
	
	farm= Farm.objects.all()
	# farm1= Farms.objects.get(id=1)
	# farm2= Farms.objects.get(id=2)
	# farm3= Farms.objects.get(id=3)
	# farm4= Farms.objects.get(id=4)
	# farm5= Farms.objects.get(id=5)
	# farm6= Farms.objects.get(id=6)
	person= Personal_info.objects.get(id=1)
	statement= Account.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	context={  'farm': farm, 'scheme': scheme, 'person': person, 'statement': statement 
	}
	return render(request, "user/invest.html", context)

def investment_form_view(request, pk, *args, **kwargs):
	
	farm= Farm.objects.get(id=1)
	person= Personal_info.objects.get(id=pk)
	statement= Account.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	context={'farm': farm,  'person': person, 'scheme': scheme, 'statement': statement 
	}
	return render(request, "user/invest-form.html", context)