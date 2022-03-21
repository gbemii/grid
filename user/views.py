from django.http import HttpResponse
from django.shortcuts import render, redirect	
from .models import *
from adminstrator.models import *
from Accounts.models import *
from .forms import UserForm, User_password_update_form, User_profile_update_form, Investor_schemeForm, TransationsForm, DepositTransationsForm, WithdrawalTransationsForm
from Accounts.views import login_view
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.


# def index_view(request, *args, **kwargs):
	
	# person= request.user
	# print(person)

	# scheme= Investment_scheme.objects.all()
	# print(scheme)
	# statement= Account.objects.all()
	# a=0
	# b=1
	# c=3
	# a=b+c
	# print(a)
	# c ={'bal':balance}
	# deposit_balance=0
	# withdraw_balance=0
	
	
	# for u in balance:
	# 	if u.transaction_type=='deposit':
	# 		deposit_balance = deposit_balance + u.amount
	# 	elif u.transaction_type=='withdraw':
	# 		withdraw_balance = withdraw_balance + u.amount

	# total_balance=deposit_balance - withdraw_balance
	# tb=total_balance
	# db=deposit_balance
	# wb=withdraw_balance

	# y ={'investmentbal':scheme}
	# invested_amount=0
	# no_investment=0
	
	# for t in scheme:
	# 	if t.approval=='approved':
	# 		no_investment= no_investment+1
	# 		invested_amount = invested_amount + t.capital_invested

	
	# ti=invested_amount
	# ni=no_investment


	# context= {'person': person, 'pp1':request.user,  'scheme': scheme, 'statement': statement
	# }
	# return render(request, "user/index.html", context)




# def user_detail_view(request, pk, *args, **kwargs):
	
# 	person= User.objects.get(id=pk)
# 	trans= Transactions.objects.all()
# 	kyc= Kyc_user_info.objects.all()
# 	user= User.objects.get(id=pk)
# 	# statement= Account.objects.get(user_id=user.id)
# 	# scheme= Investment_scheme.objects.get( id=pk )
# 	context={'person': person, 'trans': trans, 'user': user
# 	}
# 	return render(request, "administrator/user-details-regular.html", context)

# def user_update_view(request, pk, *args, **kwargs):
	
# 	person= User.objects.get(id=pk)
# 	user= User.objects.get(id=pk)


# 	form= UserForm(request.POST or None, instance= user)
# 	if form.is_valid():
# 		form.save()
# 		# return redirect('investment_list/')
	
# 	context={'person': person, 'form': form, 'user': user
# 	}
# 	return render(request, "administrator/user-update.html", context)


	


def investment_view(request, *args, **kwargs):
	
	person= request.user.id
	statement= Account.objects.all()
	scheme= Investment_scheme.objects.filter(user_id=person)
	scheme_no= Investment_scheme.objects.filter(user_id=person).count()
	# scheme= Investment_scheme.objects.all().filter(person)
	context={'person': person, 'scheme': scheme, 'scheme_no': scheme_no,'statement': statement 
	}
	return render(request, "user/schemes.html", context)

def investment_details_view(request, pk, *args, **kwargs):
	scheme= Investment_scheme.objects.get(investment_id=pk)
	# person= User.objects.get(id= scheme.user_id)
	# statement= Account.objects.get(id=1)
	context={ 'scheme': scheme
	}
	return render(request, "user/scheme-details.html", context)

def account_view(request, *args, **kwargs):
	person= request.user
	statement= Account.objects.all()
	context= {'person': person, 'statement': statement
	}
	return render(request, "user/index.html", context)


def user_profile_update_view(request, *args, **kwargs):
	
	person= request.user
	# user= User.objects.get(id=pk)
	form= User_profile_update_form(request.POST or None, instance= person)
	if form.is_valid():
		form.save()
		# return redirect('investment_list/')
	
	context={'person': person,  'form': form
	}
	return render(request, "user/user_profile_update.html", context)

def user_password_update_view(request, *args, **kwargs):
	
	person= request.user
	# user= User.objects.get(id=pk)
	if request.method == 'POST':		
		form= User_password_update_form(data= request.POST or None, user= person)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/login/')

		else:
			return redirect('/change_password')
	
	else:
		form= User_password_update_form(data= request.POST or None, user= person)
	
	context={'person': person,  'form': form
	}
	return render(request, "user/user_password_update.html", context)

def Update_plan(request):
	person= request.user


	form= Personal_infoForm(instance=person)
	context= { 'form':form, 'person':person }
	return render(request,'user/updateplan.html', context )

def deposit_form(request):
	form = DepositTransationsForm(request.POST or None)
	person= request.user
	# statement= Account.objects.filter(user_id =1)
	context= { 'form':form, 'person':person  }
	if form.is_valid():
		form.save()
		context['form']= DepositTransationsForm()

	return render(request,'user/depositing.html', context )

def withdraw_form(request):
	form = WithdrawalTransationsForm(request.POST or None)
	person= request.user
	# statement= Account.objects.filter(user_id =1)
	context= { 'form':form, 'person':person  }
	if form.is_valid():
		form.save()
		context['form']= WithdrawalTransationsForm()

	return render(request,'user/withdraw.html', context )

def farm_view(request, *args, **kwargs):
	
	farm= Farm.objects.all()
	# farm1= Farms.objects.get(id=1)
	# farm2= Farms.objects.get(id=2)
	# farm3= Farms.objects.get(id=3)
	# farm4= Farms.objects.get(id=4)
	# farm5= Farms.objects.get(id=5)
	# farm6= Farms.objects.get(id=6)
	person= request.user
	statement= Account.objects.all()
	scheme= Investment_scheme.objects.all()
	context={  'farm': farm, 'scheme': scheme, 'person': person, 'statement': statement 
	}
	return render(request, "user/invest.html", context)

def investment_form_view(request, *args, **kwargs):
	form = Investor_schemeForm(request.POST or None)
	person= request.user
	farm= Farm.objects.all()

	
	scheme= Investment_scheme.objects.all()
	context={'farm': farm,  'person': person, 'scheme': scheme, 'form': form 
	}
	if form.is_valid():
		form.save()
		context['form']= WithdrawalTransationsForm()

	return render(request, "user/invest-form.html", context)


def profile_view(request, *args, **kwargs):
	person= request.user
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.all()
	context= {'person': person, 'scheme': scheme, 'statement': statement
	}
	return render(request, "user/profile.html", context)


def setting_view(request, *args, **kwargs):
	
	person= request.user
	context={'person': person, 'first': 'joe'
	}
	return render(request, "user/profile-setting.html", context)


def login_activity_view(request, *args, **kwargs):
	print(args, kwargs)
	person= request.user
	context={'person': person, 'first': 'joe'
	}
	return render(request, "user/profile-activity.html", context)

