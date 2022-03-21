from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from user.models import *
from .models import User
from adminstrator.models import *

# Create your views here.
from user.forms import UserForm
def register_view(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user_obj= form.save()
		return redirect('/login')
		
	context = { "form": form }

	return render(request, "Accounts/auth-register.html", context )



def login_view(request):
	if request.method== "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			if user is not None and user.is_admin: 
				login(request, user)
				return redirect(admin_view)
			elif user is not None and user.is_client:
				# kk=user.id
				login(request, user)
				return redirect(client_view)
			else:
		 		pass
	#		msg= "invalid credentials"

			# login(request, user)
			# return redirect('/admin')

	else:
		form = AuthenticationForm(request)

	# msg =None
	# if request.method== "POST":
	# 	username = request.POST.get("username")
	# 	password = request.POST.get("password")
	# 	print(username, password)

	# 	user = authenticate(request, username=username, password=password)
	# 	if user is not None and user.is_admin: 
	# 		login(request, user)
	# 		return redirect('adminpage')
	# 	elif user is not None and user.is_client: 
	# 		login(request, user)
	# 		return redirect(clientpage)
	# 	else:
	#		msg= "invalid credentials"
	# else:
	# 	msg="error validating form"		
	# context= {"form":form, "msg":msg}
	context= {"form":form}
	return render(request, "Accounts/auth-login-v2.html", context)


def admin_view(request):
	# person= User.objects.get(id=pk)
	scheme= Investment_scheme.objects.all()
	statement= Account.objects.all()
	balance=Transactions.objects.all()
	inv= Investment_scheme.objects.all()
	# inv= Investment_scheme.objects.last()
	# inv= Investment_scheme.objects.filter('created_at')
	# scheme= Investment_scheme.objects.all().count()
	inv= Investment_scheme.objects.all()[:4]

	c ={'bal':balance, 'inv':scheme}








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

	# plan={'plans':scheme}
	

	# poultry={}
	# pig={}
	# maize={}
	# rice={}
	# cow={}
	# sheepndgoat={}
	poultry=0
	pig=0.5
	maize=0.5
	rice=0
	cow=0
	sheepndgoat=0

	count=0

	for st in scheme:
		if st.name_of_scheme =='Poultry Farming' and f.investment_status == 'approved':
			poultry = poultry + 1
			print(poultry)
		elif st.name_of_scheme =='Pig Rearing' and f.investment_status == 'approved':
			pig = pig + 1
			print(pig)
		elif st.name_of_scheme =='Maize Farming' and f.investment_status == 'approved':
			maize =  maize + 1
			print(maize)
		elif st.name_of_scheme =='Rice Farming' and f.investment_status == 'approved':
			rice =  rice + 1
			print(rice)
		elif st.name_of_scheme =='Cow Sponsorship' and f.investment_status == 'approved':
			cow =  cow + 1
			print(cow)
		elif st.name_of_scheme =='Sheep and Goat Rearing' and f.investment_status == 'approved':
			sheepndgoat =  sheepndgoat + 1
			print(sheepndgoat)
		else:
			pass


	# # poultrylen=len(poultry)
	# piglen=len(pig)
	# maizelen=len(maize)
	# ricelen=len(rice)
	# cowlen=len(cow)
	# sheepndgoatlen=len(sheepndgoat)

	# totallen=1
	totallen=poultry+pig+maize+rice+cow+sheepndgoat
	print(totallen)
	poultrylen=(poultry/totallen) *100
	piglen=(pig/totallen) *100
	maizelen=(maize/totallen) *100
	ricelen=(rice/totallen) *100
	cowlen=(cow/totallen) *100
	sheepndgoatlen=(sheepndgoat/totallen) *100




	
	
	context= {'c':c,'inv':inv, 'scheme': scheme, 'count': count, 'statement': statement, 'balance': balance ,'db':db,'wb':wb,'tb':tb,
				'ti':ti, 'ni':ni,
				'poultrylen': poultrylen, 'piglen': piglen,'maizelen': maizelen,'ricelen': ricelen,'cowlen': cowlen,'sheepndgoatlen': sheepndgoatlen
	}
	return render(request,'administrator/index.html', context)

def client_view(request, *args, **kwargs):
	person= request.user
	print(person)

	# person= User.objects.get(id=agent)
	# if person is not None and person.is_admin: 
	# 	login(request, person)
	# 	# pk=user.id
	# 	# print(pk)
	# 	return redirect(admin_view)

	# else:
	scheme1= Investment_scheme.objects.all().filter(user_id=person)[:4]
	scheme_no= Investment_scheme.objects.filter(user_id=person).count()
	statement= Account.objects.all()


	
	context= {'person': person, 'scheme': scheme1, 'scheme_no': scheme_no, 'statement': statement
	}

	
	return render(request,'user/index.html', context)



def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect("/login/")


	context={ }
	return render(request, "Accounts/auth-logout-v2.html",context)


# def register():
# 	if request.method== "POST":
# 		username =request.POST['username']
# 		email =request.POST['email']
# 		password =request.POST['password']

# 		if User.objects.filter(username=username).exists():
# 			print("username exists try another one")
# 			return redirect('register')
# 		else:
# 			if User.objects.filter(email=email).exists():
# 				print("email exists try another one")
# 				return redirect('register')

# 			else:
# 				user= User.objects.create_user(username=username, email=email, password=password)
# 				user.save()
# 				return redirect('login')

# 	else:
# 		return render(request, 'Accounts/auth-register.html')
		
