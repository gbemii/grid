from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def register():
	if request.method== "POST":
		username =request.POST['username']
		email =request.POST['email']
		password =request.POST['password']

		if User.objects.filter(username=username).exists():
			print("username exists try another one")
			return redirect('register')
		else:
			if User.objects.filter(email=email).exists():
				print("email exists try another one")
				return redirect('register')

			else:
				user= User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')

	else:
		return render(request, 'Accounts/auth-register.html')
		
