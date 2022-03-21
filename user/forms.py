from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Transactions, Investment_scheme  
from Accounts.models import User
from adminstrator.models import Farm
class UserForm(UserCreationForm):
	class Meta:
		model= User
		fields= ['username','email','password1','password2']

class TransationsForm(ModelForm):
	class Meta:
		model= Transactions
		fields= ['approval']

class WithdrawalTransationsForm(ModelForm):
	class Meta:
		model= Transactions
		fields= ['user_id', 'transaction_type', 'amount']


class DepositTransationsForm(ModelForm):
	class Meta:
		model= Transactions
		fields= ['user_id', 'transaction_type', 'amount', 'reciept_upload']

class Investment_schemeForm(ModelForm):
	class Meta:
		model= Investment_scheme
		fields= ['investment_status']

class Investor_schemeForm(ModelForm):
	class Meta:
		model= Investment_scheme
		fields= ['user_id', 'name_of_scheme', 'capital_invested']

class FarmForm(ModelForm):
	class Meta:
		model= Farm
		fields= '__all__'

class User_profile_update_form(ModelForm):
	class Meta:
		model= User
		fields= '__all__'


class User_password_update_form(PasswordChangeForm):
	class Meta:
		model= User
		fields= ['password']