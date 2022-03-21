from django.db import models
from Accounts.models import User
from adminstrator.models import Farm

# Create your models here.


class Personal_info(models.Model):
	firstname =models.CharField(max_length=225)
	surname= models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	phone_number= models.CharField(max_length=2555)
	date_of_birth= models.CharField(max_length=255)
	address_line1= models.CharField(max_length=255)
	address_line2= models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	Password= models.CharField(max_length=222)
	state=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	nationality=models.CharField(max_length=20)
	document_upload= models.CharField(max_length=2222)
	telegram_username=models.CharField(max_length=222)
	blocked=models.BooleanField(default=False)

	def __str__(self):
		return self.firstname


my_choices=(('approved', 'approved'),('pending', 'pending'),('inactive', 'inactive'))

class Investment_scheme(models.Model):
	investment_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	user_id= models.ForeignKey(User, on_delete=models.CASCADE)
	name_of_scheme= models.ForeignKey(Farm, on_delete=models.CASCADE)
	capital_invested= models.IntegerField()
	investment_status= models.CharField(max_length=222, choices=my_choices)
	monthly_profit= models.IntegerField(default= 1, blank=True, null=True)
	net_profit= models.IntegerField( default= 1, blank=True, null=True)
	term_of_scheme= models.IntegerField(default= 1, blank=True, null=True)
	term_begins= models.DateTimeField(auto_now=True)
	term_ends= models.DateTimeField(auto_now=True)
	initiation_date= models.DateTimeField(auto_now_add=True)
	approved_date= models.DateTimeField(auto_now=True)
	viewed=models.BooleanField(default=False)
	


	def __str__(self):
		return str (self.investment_id)


class Account(models.Model):
	investment_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	user_id= models.ForeignKey(User, on_delete=models.CASCADE)
	available_funds= models.IntegerField()
	invested_funds= models.IntegerField()
	account_balance= models.IntegerField()
	total_profit= models.IntegerField()
	open_postions= models.IntegerField()



	def __str__(self):
		return str (self.investment_id)


class Transactions(models.Model):
	transaction_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	user_id= models.ForeignKey(User, on_delete=models.CASCADE)
	transaction_type= models.CharField(max_length=222)
	amount= models.IntegerField()
	initiation_date= models.DateTimeField(auto_now_add=True)
	reciept_upload= models.FileField(upload_to='uploads', blank=True)
	approval=models.BooleanField(default=False)
	viewed=models.BooleanField(default=False)

	def __str__(self):
		return str (self.transaction_id)

class Kyc_user_info(models.Model):
	firstname =models.CharField(max_length=225)
	surname= models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	phone_number= models.CharField(max_length=2555)
	date_of_birth= models.CharField(max_length=255)
	address_line1= models.CharField(max_length=255)
	address_line2= models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	Password= models.CharField(max_length=222)
	state=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	nationality=models.CharField(max_length=20)
	document_upload= models.CharField(max_length=2222)
	telegram_username=models.CharField(max_length=222)

	def __str__(self):
		return self.firstname



# class Farms(models.Model):
# 	farm_id =models.CharField(max_length=225)
# 	farm_name= models.CharField(max_length=222)
# 	monthly_interest= models.CharField(max_length=222)
# 	terms= models.CharField(max_length=222)
# 	roi= models.CharField(max_length=222)
# 	apy= models.CharField(max_length=222)
# 	farm_description= models.CharField(max_length=222)



# 	def __str__(self):
# 		return self.farm_id

