from django.http import HttpResponse
from django.shortcuts import render
from adminstrator.models import Admin_info, Farm
from user.models import *
# from .forms import *
# Create your views here.


def admin_index_view(request, pk, *args, **kwargs):
	person= Admin_info.objects.get(id=pk)
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.get(id=1)
	balance=Transactions.objects.all()
	c ={'bal':balance}
	deposit_balance=0
	withdraw_balance=0
	
	# for i in balance:
	# 	total_balance = total_balance + i.amount

	# tb=total_balance
	
	for u in balance:
		if u.transaction_type=='deposit':
			deposit_balance = deposit_balance + u.amount
		elif u.transaction_type=='withdraw':
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
		if t.approval=='approved':
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

		if f.name_of_scheme =='poultry':
			poultry = poultry + 1
		elif f.name_of_scheme =='pig':
			pig = pig+ 1
		elif f.name_of_scheme =='maize':
			maize =  maize + 1
		elif f.name_of_scheme =='rice':
			rice =  rice + 1
		elif f.name_of_scheme =='cow':
			cow =  cow + 1
		elif f.name_of_scheme =='sheep and goat':
			sheepndgoat =  sheepndgoat + 1

	# # poultrylen=len(poultry)
	# piglen=len(pig)
	# maizelen=len(maize)
	# ricelen=len(rice)
	# cowlen=len(cow)
	# sheepndgoatlen=len(sheepndgoat)

	poultrylen=poultry
	piglen=pig
	maizelen=maize
	ricelen=rice
	cowlen=cow
	sheepndgoatlen=sheepndgoat


	
	
	context= {'person': person, 'scheme': scheme, 'statement': statement, 'balance': balance ,'db':db,'wb':wb,'tb':tb,
				'ti':ti, 'ni':ni,
				'poultrylen': poultrylen, 'piglen': piglen,'maizelen': maizelen,'ricelen': ricelen,'cowlen': cowlen,'sheepndgoatlen': sheepndgoatlen
	}
	print(sheepndgoatlen)
	print(poultrylen)
	print(piglen)
	print(maizelen)
	print(ricelen)
	print(cowlen)
	print(sheepndgoatlen)

	return render(request, "administrator/index.html", context)

def farm_views(request, pk, *args, **kwargs):
	farm= Farm.objects.all()
	person= Admin_info.objects.get(id=pk)
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

		print(i.id)
	context={ 'person': person,'farm': farm }
	return render(request, "administrator/farm_list.html", context)

def farm_details_views(request, pk, *args, **kwargs):
	
	farm= Farm.objects.get(id=pk)
	person= Admin_info.objects.get(id=1)
	
	context={ 'person': person,'farm': farm }
	return render(request, "administrator/invoice-details.html", context)



def transaction_view(request, *args, **kwargs):
	person= Admin_info.objects.get(id=1)
	trans= Transactions.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'trans': trans, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/transaction-basic.html", context)

def investment_list(request, *args, **kwargs):
	person= Admin_info.objects.get(id=1)
	trans= Transactions.objects.all()
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.get(id=1)
	context= {'person': person, 'trans': trans, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/investment.html", context)

def investment_detail_view(request, pk, *args, **kwargs):
	
	person= Personal_info.objects.get(id=pk)
	statement= Account.objects.get(id=1)
	scheme= Investment_scheme.objects.get( id=pk )
	context={'person': person, 'scheme': scheme, 'statement': statement 
	}
	return render(request, "administrator/investment-details.html", context)

def user_list_view(request, *args, **kwargs):
	person= Admin_info.objects.get(id=1)
	trans= Transactions.objects.all()
	kyc= Kyc_user_info.objects.all()
	user= Personal_info.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'trans': trans, 'user': user, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-list-regular.html", context)

def user_detail_view(request, pk, *args, **kwargs):
	
	person= Personal_info.objects.get(id=pk)
	trans= Transactions.objects.all()
	kyc= Kyc_user_info.objects.all()
	user= Personal_info.objects.get(id=pk)
	statement= Account.objects.get(id=pk)
	# scheme= Investment_scheme.objects.get( id=pk )
	context={'person': person, 'trans': trans, 'user': user, 'statement': statement 
	}
	return render(request, "administrator/user-details-regular.html", context)

def kyc_list_view(request, *args, **kwargs):
	person= Admin_info.objects.get(id=1)
	trans= Transactions.objects.all()
	kyc= Kyc_user_info.objects.all()
	user= Kyc_user_info.objects.all()
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'trans': trans, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/kyc-list-regular.html", context)

def admin_profile_view(request, pk, *args, **kwargs):
	person= Admin_info.objects.get(id=pk)
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-profile-regular.html", context)


def admin_profile_setting_view(request, pk, *args, **kwargs):
	person= Admin_info.objects.get(id=pk)
	scheme= Investment_scheme.objects.get(id=1)
	statement= Account.objects.get(id=1)
	context= {'person': person, 'scheme': scheme, 'statement': statement
	}
	return render(request, "administrator/user-profile-setting.html", context)

# def faqs_view(request, pk, *args, **kwargs):
# 	person= Admin_info.objects.get(id=pk)
# 	scheme= Investment_scheme.objects.get(id=1)
# 	statement= Account.objects.get(id=1)
# 	context= {'person': person, 'scheme': scheme, 'statement': statement
# 	}
# 	return render(request, "administrator/faqs.html", context)

# def terms_policy_view(request, pk, *args, **kwargs):
# 	person= Admin_info.objects.get(id=pk)
# 	scheme= Investment_scheme.objects.get(id=1)
# 	statement= Account.objects.get(id=1)
# 	context= {'person': person, 'scheme': scheme, 'statement': statement
# 	}
# 	return render(request, "administrator/terms-policy.html", context)


