from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from adminstrator.models import Admin_info, Farm
from user.models import *
from user.forms import UserForm, FarmForm, Investment_schemeForm, TransationsForm
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def admin_index_view(request, pk, *args, **kwargs):
	person= User.objects.get(id=pk)
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.all()
	balance=Transactions.objects.all()
	c ={'bal':balance}
	deposit_balance=0
	withdraw_balance=0
	
	# for i in balance:
	# 	total_balance = total_balance + i.amount

	# tb=total_balance
	
	for u in balance:
		if u.transaction_type=='deposit' and u.approval is True:
			deposit_balance = deposit_balance + u.amount
		elif u.transaction_type=='withdraw' and u.approval is True:
			withdraw_balance = withdraw_balance + u.amount

	total_balance=deposit_balance - withdraw_balance
	tb=total_balance
	db=deposit_balance
	wb=withdraw_balance

	# for b in c:  
	#   total_balance= sum(b.amount)
	# print(total_balance)

	# total investment amount
	y ={'investmentbal':scheme}
	invested_amount=0
	no_investment=0
	
	for t in scheme:
		if t.investment_status=='approved':
			no_investment= no_investment+1
			invested_amount = invested_amount + t.capital_invested

	
	ti=invested_amount
	ni=no_investment

	plan={'plans':scheme}
	

	# poultry={}
	# pig={}
	# maize={}
	# rice={}
	# cow={}
	# sheepndgoat={}
	poultry=0
	pig=0
	maize=0
	rice=0
	cow=0
	sheepndgoat=0

	for f in scheme :

		if f.name_of_scheme =='Poultry' and f.investment_status == 'approved':
			poultry = poultry + 1
		elif f.name_of_scheme =='Pig rearing' and f.investment_status == 'approved':
			pig = pig + 1
		elif f.name_of_scheme =='Maize Farming' and f.investment_status == 'approved':
			maize =  maize + 1
		elif f.name_of_scheme =='Rice Farming' and f.investment_status == 'approved':
			rice =  rice + 1
		elif f.name_of_scheme =='Cow Sponsorship' and f.investment_status == 'approved':
			cow =  cow + 1
		elif f.name_of_scheme =='Sheep and Goat Rearing' and f.investment_status == 'approved':
			sheepndgoat =  sheepndgoat + 1

	# # poultrylen=len(poultry)
	# piglen=len(pig)
	# maizelen=len(maize)
	# ricelen=len(rice)
	# cowlen=len(cow)
	# sheepndgoatlen=len(sheepndgoat)
	totallen=0
	totallen=poultry+pig+maize+rice+cow+sheepandgoat
	poultrylen=(poultry/totallen) *100
	piglen=(pig/totallen) *100
	maizelen=(maize/totallen) *100
	ricelen=(rice/totallen) *100
	cowlen=(cow/totallen) *100
	sheepndgoatlen=(sheepndgoat/totallen) *100


	print(sheepndgoatlen)
	print(poultrylen)
	print(piglen)
	print(maizelen)
	print(ricelen)
	print(cowlen)
	print(sheepndgoatlen)
	
	context= {'person': person, 'agent': agent, 'scheme': scheme, 'statement': statement, 'balance': balance ,'db':db,'wb':wb,'tb':tb,
				'ti':ti, 'ni':ni,
				'poultrylen': poultrylen, 'piglen': piglen,'maizelen': maizelen,'ricelen': ricelen,'cowlen': cowlen,'sheepndgoatlen': sheepndgoatlen
	}
	

	return render(request, "administrator/index.html", context)

def farm_views(request, *args, **kwargs):
	farm= Farm.objects.all()
	agent= request.user
	# farm1= Farms.objects.get(id=1)
	# farm2= Farms.objects.get(id=2)
	# farm3= Farms.objects.get(id=3)
	# farm4= Farms.objects.get(id=4)
	# farm5= Farms.objects.get(id=5)
	# farm6= Farms.objects.get(id=6)
	# person= Personal_info.objects.get(id=1)
	# statement= Account.objects.get(id=1)
	# scheme= Investment_scheme.objects.get(id=1)
	# context={ 'farm1': farm1, 'farm2': farm2, 
	# 'farm3': farm3, 'farm4': farm4, 'farm5': farm5, 'farm6': farm6,
	#  'scheme': scheme, 'person': person, 'statement': statement 
	# }
	fa={'nu':farm}
	for i in farm:

		print(i.farm_id)
	context={ 'agent': agent, 'farm': farm }
	return render(request, "administrator/farm_list.html", context)

def farm_details_views(request, pk, *args, **kwargs):
	
	farm= Farm.objects.get(farm_id=pk)
	agent = request.user
	
	context={ 'agent': agent, 'farm': farm }
	return render(request, "administrator/farm-details.html", context)

def farm_update_view(request, pk, *args, **kwargs):
	
	agent= request.user
	farm= Farm.objects.get(farm_id=pk)


	form= FarmForm(request.POST or None, instance= farm)
	if form.is_valid():
		form.save()
		# return redirect('investment_list/')
	
	context={ 'agent': agent, 'form': form, 'farm': farm
	}
	return render(request, "administrator/farm-update.html", context)



def transaction_view(request, *args, **kwargs):
	agent= request.user
	
	trans= Transactions.objects.all()
	# scheme= Investment_scheme.objects.get(id=1)
	# statement= Account.objects.get(id=1)
	context= {'agent': agent, 'trans': trans
	}
	return render(request, "administrator/transaction-basic.html", context)

def transaction_detail_view(request, pk, *args, **kwargs):
	agent= request.user
	# person= request.user
	# statement= Account.objects.get(id=1)
	trans= Transactions.objects.get(transaction_id=pk)
	context={ 'agent': agent, 'trans': trans
	}
	return render(request, "administrator/transaction-details.html", context)

def transaction_update_view(request, pk, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=pk)

	trans= Transactions.objects.get(transaction_id=pk )
	form= TransationsForm(request.POST or None, instance= trans)
	if form.is_valid():
		form.save()
		# return redirect('investment_list/')
	
	context={'person': person, 'agent': agent, 'form': form, 'trans': trans
	}
	return render(request, "administrator/transaction-update.html", context)

def investment_list(request, *args, **kwargs):
	agent= request.user
	# trans= Transactions.objects.all()
	scheme= Investment_scheme.objects.all()
	# statement= Account.objects.get(id=1)
	context= { 'agent': agent, 'scheme': scheme
	}
	return render(request, "administrator/investment.html", context)

def investment_update_view(request, pk, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=pk)

	scheme= Investment_scheme.objects.get(investment_id=pk )
	form= Investment_schemeForm(request.POST or None, instance= scheme)
	if form.is_valid():
		form.save()
		# return redirect('investment_list/')
	
	context={'person': person, 'agent': agent, 'form': form, 'scheme': scheme
	}
	return render(request, "administrator/investment-update.html", context)


# def investment_detail_view(request, pk, *args, **kwargs):
	
# 	person= User.objects.get(id=pk)

# 	# statement= Account.objects.get(id=1)
# 	scheme= Investment_scheme.objects.get(investment_id=pk )
# 	form= Investment_schemeForm(request.POST or None, instance= scheme)
# 	if form.is_valid():
# 		form.save()
# 		# return redirect('investment_list/')
	
# 	context={'person': person, 'form': form, 'scheme': scheme
# 	}
# 	return render(request, "administrator/investment-details.html", context)

def investment_detail_view(request, pk, *args, **kwargs):
	agent= request.user
	# person= User.objects.get(id=pk)
	# statement= Account.objects.get(id=1)
	scheme= Investment_scheme.objects.get(investment_id=pk )
	context={ 'agent': agent, 'scheme': scheme
	}
	return render(request, "administrator/investment-details.html", context)


def user_list_view(request, *args, **kwargs):
	# agent= request.user
	person= User.objects.all()
	trans= Transactions.objects.all()
	# kyc= Kyc_user_info.objects.all()
	# user= User.objects.all()
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.all()
	context= {'person': person,  'trans': trans,  'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-list-regular.html", context)

def user_detail_view(request, pk, *args, **kwargs):
	# agent= request.user
	person= User.objects.get(id=pk)
	trans= Transactions.objects.all()
	kyc= Kyc_user_info.objects.all()
	# user= User.objects.get(id=pk)
	# statement= Account.objects.get(user_id=user.id)
	# scheme= Investment_scheme.objects.get( id=pk )
	context={'person': person,  'trans': trans
	}
	return render(request, "administrator/user-details-regular.html", context)

def user_update_view(request, pk, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=pk)
	# user= User.objects.get(id=pk)


	form= UserForm(request.POST or None, instance= person)
	if form.is_valid():
		form.save()
		# return redirect('investment_list/')
	
	context={'person': person, 'agent': agent, 'form': form
	}
	return render(request, "administrator/user-update.html", context)

def kyc_list_view(request, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=1)
	trans= Transactions.objects.all()
	kyc= Kyc_user_info.objects.all()
	user= Kyc_user_info.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.filter(id=1)
	context= {'person': person, 'agent': agent, 'trans': trans, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/kyc-list-regular.html", context)

def admin_profile_view(request, pk, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=pk)
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'agent': agent, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-profile-regular.html", context)

@login_required
def admin_profile_setting_view(request, pk, *args, **kwargs):
	agent= request.user
	person= User.objects.get(id=pk)
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'agent': agent, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-profile-setting.html", context)

# def faqs_view(request, pk, *args, **kwargs):
# 	person= User.objects.get(id=pk)
# 	scheme= Investment_scheme.objects.get(id=1)
# 	statement= Account.objects.get(id=1)
# 	context= {'person': person, 'scheme': scheme, 'statement': statement
# 	}
# 	return render(request, "administrator/faqs.html", context)

# def terms_policy_view(request, pk, *args, **kwargs):
# 	person= User.objects.get(id=pk)
# 	scheme= Investment_scheme.objects.get(id=1)
# 	statement= Account.objects.get(id=1)
# 	context= {'person': person, 'scheme': scheme, 'statement': statement
# 	}
# 	return render(request, "administrator/terms-policy.html", context)

def admin_password_update_view(request, *args, **kwargs):
	
	person= request.user
	# user= User.objects.get(id=pk)
	if request.method == 'POST':		
		form= PasswordChangeForm(data= request.POST or None, user= person)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/login/')

		else:
			return redirect('/change_password')
	
	else:
		form= PasswordChangeForm(data= request.POST or None, user= person)
	
	context={'person': person,  'form': form
	}
	return render(request, "administrator/admin_password_update.html", context)
